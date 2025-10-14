import pytest
from specmatic.core.specmatic import Specmatic
from specmatic.coverage.servers.flask_app_coverage_server import FlaskAppCoverageServer
from specmatic.servers.wsgi_app_server import WSGIAppServer

from test import APP, APP_HOST, APP_PORT, ROOT_DIR, MOCK_HOST, MOCK_PORT, expectation_json_files

app_server = WSGIAppServer(APP, APP_HOST, APP_PORT)
coverage_server = FlaskAppCoverageServer(APP)

app_server.start()
coverage_server.start()


class TestContract:
    pass


Specmatic().with_project_root(ROOT_DIR).with_mock(MOCK_HOST, MOCK_PORT, expectation_json_files).with_endpoints_api(
    coverage_server.endpoints_api,
).test(TestContract, APP_HOST, APP_PORT).run()

app_server.stop()
coverage_server.stop()

if __name__ == "__main__":
    pytest.main()
