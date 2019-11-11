"""
Test API load endpoint
~~~~~~~~~~~~~~~~~~~~~~
"""
import json as _json

import pytest as _pytest
from falcon import testing as _testing

from power_net.app.api import server as _server
from power_net.app.api import _resources

MOCKIT = _resources


@_pytest.fixture()
def setup_client():
    """
    Setup Falcon API for testing
    """
    return _testing.TestClient(_server._create_api())


def test_load_get(mockit, setup_client):
    """
    Test GET request
    """
    client = setup_client
    network = mockit('_network')
    data = {'foo': 'bar'}
    data_json = _json.dumps(data)
    network.net.get_load_res.return_value = data_json

    result = client.simulate_get(path='/api/load')
    assert result.status_code == 200
    assert result.json == data


def test_generator_get(mockit, setup_client):
    """
    Test GET request
    """
    client = setup_client
    network = mockit('_network')
    data = {'foo': 'bar'}
    data_json = _json.dumps(data)
    network.net.get_generator_res.return_value = data_json

    result = client.simulate_get(path='/api/generator')
    assert result.status_code == 200
    assert result.json == data
