import pytest
from specmatic.core.decorators import specmatic_contract_test, specmatic_mock, start_wsgi_app

from test import APP, APP_HOST, APP_PORT, ROOT_DIR, MOCK_HOST, MOCK_PORT, expectation_json_files


# NOTE: Type Hint AppRouteAdapter in specmatic_contract_test decorator should be AppRouteAdapter | None
@specmatic_contract_test(APP_HOST, APP_PORT, ROOT_DIR)  # type: ignore[reportArgumentType]
@start_wsgi_app(APP, APP_HOST, APP_PORT)
@specmatic_mock(MOCK_HOST, MOCK_PORT, ROOT_DIR, expectation_json_files)
class TestApiContract:
    pass


if __name__ == "__main__":
    pytest.main()
