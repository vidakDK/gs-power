"""
Fixtures specific to API testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import pytest as _pytest

from falcon import testing as _testing

from power_net.app.api import server as _server


@_pytest.fixture()
def setup_client():
    """
    Setup Falcon API for testing
    """
    return _testing.TestClient(_server._create_api())
