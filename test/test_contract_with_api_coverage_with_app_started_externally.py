import pytest
from specmatic.core.specmatic import Specmatic
from specmatic.servers.wsgi_app_server import WSGIAppServer

from definitions import PROJECT_ROOT
from test import APP, APP_HOST, APP_PORT

app_server = WSGIAppServer(APP, APP_HOST, APP_PORT)
app_server.start()


class TestContract:
    pass


try:
    (
        Specmatic(PROJECT_ROOT)
        .with_mock()
        .test_with_api_coverage_for_flask_app(TestContract, APP, APP_HOST, APP_PORT)
        .run()
    )
finally:
    app_server.stop()

if __name__ == "__main__":
    pytest.main()
