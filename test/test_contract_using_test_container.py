import os
import sys
import threading
from pathlib import Path
from wsgiref.simple_server import make_server

import pytest
from testcontainers.core.container import DockerContainer
from testcontainers.core.wait_strategies import HttpWaitStrategy, LogMessageWaitStrategy

from api import app

APPLICATION_HOST = "0.0.0.0"
APPLICATION_PORT = 5000
HTTP_STUB_PORT = 8080


def stream_container_logs(container: DockerContainer, name=None):
    def _stream():
        for line in container.get_wrapped_container().logs(stream=True, follow=True):
            text = line.decode(errors="ignore").rstrip()
            prefix = f"[{name}] " if name else ""
            print(f"{prefix}{text}")

    thread = threading.Thread(target=_stream, daemon=True)
    thread.start()
    return thread


@pytest.fixture(scope="module")
def api_service():
    server = make_server(APPLICATION_HOST, APPLICATION_PORT, app)
    thread = threading.Thread(target=server.serve_forever)
    thread.start()
    yield
    server.shutdown()
    thread.join()


@pytest.fixture(scope="module")
def stub_container():
    examples_path = Path("test/data").resolve()
    specmatic_yaml_path = Path("specmatic.yaml").resolve()
    build_reports_path = Path("build/reports/specmatic").resolve()
    container = (
        DockerContainer("specmatic/specmatic")
        .with_command(["virtualize", "--examples=examples", f"--port={HTTP_STUB_PORT}"])
        .with_bind_ports(HTTP_STUB_PORT, HTTP_STUB_PORT)
        .with_volume_mapping(examples_path, "/usr/src/app/examples", mode="ro")
        .with_volume_mapping(specmatic_yaml_path, "/usr/src/app/specmatic.yaml", mode="ro")
        .with_volume_mapping(build_reports_path, "/usr/src/app/build/reports/specmatic", mode="rw")
        .waiting_for(HttpWaitStrategy(HTTP_STUB_PORT, path="/actuator/health").with_method("GET").for_status_code(200))
    )
    container.start()
    stream_container_logs(container, name="specmatic-stub")
    yield container
    container.stop()


@pytest.fixture(scope="module")
def test_container():
    specmatic_yaml_path = Path("specmatic.yaml").resolve()
    build_reports_path = Path("build/reports/specmatic").resolve()
    container = (
        DockerContainer("specmatic/specmatic")
        .with_command(["test", "--host=host.docker.internal", f"--port={APPLICATION_PORT}"])
        .with_env("SPECMATIC_GENERATIVE_TESTS", "true")
        .with_volume_mapping(specmatic_yaml_path, "/usr/src/app/specmatic.yaml", mode="ro")
        .with_volume_mapping(build_reports_path, "/usr/src/app/build/reports/specmatic", mode="rw")
        .with_kwargs(extra_hosts={"host.docker.internal": "host-gateway"})
        .waiting_for(LogMessageWaitStrategy("Tests run:"))
    )
    container.start()
    stream_container_logs(container, name="specmatic-test")
    yield container
    container.stop()


@pytest.mark.skipif(
    os.environ.get("CI") == "true" and not sys.platform.startswith("linux"),
    reason="Run only on Linux CI; all platforms allowed locally",
)
def test_contract(api_service, stub_container, test_container):
    stdout, stderr = test_container.get_logs()
    stdout = stdout.decode("utf-8")
    stderr = stderr.decode("utf-8")
    if stderr or "Failures: 0" not in stdout:
        raise AssertionError(f"Contract tests failed; container logs:\n{stdout}\n{stderr}")  # noqa: EM102
