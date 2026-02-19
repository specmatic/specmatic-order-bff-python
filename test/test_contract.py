import pytest
from specmatic.core.specmatic import Specmatic

from definitions import PROJECT_ROOT
from test import APP, APP_HOST, APP_PORT


class TestContract:
    pass


(
    Specmatic(PROJECT_ROOT)
    .with_mock()
    .with_wsgi_app(APP, APP_HOST, APP_PORT)
    .test(TestContract)
    .run()
)

if __name__ == "__main__":
    pytest.main()
