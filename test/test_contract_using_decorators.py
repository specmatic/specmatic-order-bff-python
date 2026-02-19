import pytest
from specmatic.core.decorators import specmatic_contract_test, specmatic_mock, start_wsgi_app

from definitions import PROJECT_ROOT
from test import APP, APP_HOST, APP_PORT


# NOTE: Type Hint AppRouteAdapter in specmatic_contract_test decorator should be AppRouteAdapter | None
@specmatic_contract_test(project_root=PROJECT_ROOT)  # type: ignore[reportArgumentType]
@start_wsgi_app(APP, APP_HOST, APP_PORT)
@specmatic_mock(project_root= PROJECT_ROOT)
class TestApiContract:
    pass


if __name__ == "__main__":
    pytest.main()
