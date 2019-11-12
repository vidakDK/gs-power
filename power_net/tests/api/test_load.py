"""
Test API load endpoint
~~~~~~~~~~~~~~~~~~~~~~
"""
import json as _json

import pytest as _pytest
from falcon import testing as _testing

from power_net.app.api import server as _server
from power_net.app.api import _resources
from .. import _util as _test

MOCKIT = _resources


@_pytest.fixture()
def setup_client():
    """
    Setup Falcon API for testing
    """
    return _testing.TestClient(_server._create_api())


def test_load_get(mockit, setup_client):
    """
    Test GET request - success
    """
    client = setup_client
    network = mockit('_network')
    data = {'foo': 'bar'}
    data_json = _json.dumps(data)
    network.net.get_load_res.return_value = data_json

    result = client.simulate_get(path='/api/load')
    assert result.status_code == 200
    assert result.json == data


def test_load_post_ok(mockit, setup_client):
    """
    Test Load POST request - success
    """
    client = setup_client
    network = mockit('_network')
    data = {'p_mw': 0.5, 'q_mvar': 0.15}

    result = client.simulate_post(path='/api/load', json=data)
    print(result.content)
    assert result.status_code == 200
    assert result.json is None

    _test.assert_calls(network.net, [('set_load_params', (0.5, 0.15), {})])


@_pytest.mark.parametrize('input_data', [({'p_mw': 'foo', 'q_mvar': 0.4},),
                                         ({'q_mvar': 0.4},),
                                         ('foo',)])
def test_load_post_bad_request(mockit, setup_client, input_data):
    """
    Test Load POST request - Bad Request
    """
    client = setup_client
    network = mockit('_network')

    result = client.simulate_post(path='/api/load', json=input_data)
    assert result.status_code == 400
    assert result.json == {'title': f"Request body needs to be a dictionary with active power (`p_mw`) and reactive "
                                    f"power (`q_mvar`) of the load as the key. Got {list(input_data)} instead."}

    # Assert network doesn't get called in this case at all.
    _test.assert_calls(network, [])