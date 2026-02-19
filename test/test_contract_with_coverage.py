import pytest
from specmatic.core.specmatic import Specmatic

from definitions import PROJECT_ROOT
from test import APP, APP_HOST, APP_PORT


class TestContract:
    pass


(
    Specmatic()
    .with_project_root(PROJECT_ROOT)
    .with_mock()
    .with_wsgi_app(APP, APP_HOST, APP_PORT)
    .test_with_api_coverage_for_flask_app(TestContract, APP)
    .run()
)

if __name__ == "__main__":
    pytest.main()
