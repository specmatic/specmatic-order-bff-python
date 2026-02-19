import pytest
from specmatic.core.specmatic import Specmatic

from definitions import PROJECT_ROOT_PATH, PROJECT_ROOT
from test import APP, MOCK_HOST, MOCK_PORT


class TestContract:
    pass


def set_app_config(app, host: str, port: int):
    app.config["ORDER_API_HOST"] = host
    app.config["ORDER_API_PORT"] = str(port)
    app.config["API_URL"] = f"http://{host}:{port}"


def reset_app_config(app):
    app.config["ORDER_API_HOST"] = MOCK_HOST
    app.config["ORDER_API_PORT"] = MOCK_PORT
    app.config["API_URL"] = f"http://{MOCK_HOST}:{MOCK_PORT}"


(
    Specmatic(PROJECT_ROOT)
    .with_specmatic_config_file_path(str(PROJECT_ROOT_PATH / "test" / "resources" / "specmatic_config_for_autowiring.yaml"))
    .with_mock()
    .with_wsgi_app(
        APP,
        set_app_config_func=set_app_config,
        reset_app_config_func=reset_app_config,
    )
    .test(TestContract)
    .run()
)

reset_app_config(APP)

if __name__ == "__main__":
    pytest.main()
