import os

import pytest
from specmatic.core.specmatic import Specmatic

from api import app
from definitions import ROOT_DIR
from test import expectation_json_files


class TestContract:
    pass


def set_app_config(app, host: str, port: int):
    app.config["ORDER_API_HOST"] = host
    app.config["ORDER_API_PORT"] = str(port)


def reset_app_config(app):
    app.config["ORDER_API_HOST"] = os.getenv("ORDER_API_HOST")
    app.config["ORDER_API_PORT"] = os.getenv("ORDER_API_PORT")


Specmatic().with_project_root(ROOT_DIR).with_stub(expectations=expectation_json_files).with_wsgi_app(
    app,
    set_app_config_func=set_app_config,
    reset_app_config_func=reset_app_config,
).test(TestContract).run()

reset_app_config(app)

if __name__ == "__main__":
    pytest.main()
