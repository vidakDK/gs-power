"""
Test API load endpoint
~~~~~~~~~~~~~~~~~~~~~~
"""
import json as _json

import pytest as _pytest

from power_net.app.api import _resources
from .. import _util as _test

MOCKIT = _resources


def test_generator_get(mockit, setup_client):
    """
    Test Generator GET request
    """
    client = setup_client
    network = mockit('_network')
    data = {'foo': 'bar'}
    data_json = _json.dumps(data)
    network.net.get_generator_res.return_value = data_json

    result = client.simulate_get(path='/api/generator')
    assert result.status_code == 200
    assert result.json == data


def test_generator_post_ok(mockit, setup_client):
    """
    Test Generator POST request - Success
    """
    client = setup_client
    network = mockit('_network')
    data = {'p_mw': 0.5}

    result = client.simulate_post(path='/api/generator', json=data)
    assert result.status_code == 200
    assert result.json is None

    _test.assert_calls(network.net, [('set_generator_params', (0.5,), {})])


@_pytest.mark.parametrize('input_data', [({'p_mw': 'foo'},),
                                           ({'q_mw': 0.4},),
                                           ('foo',)])
def test_generator_post_bad_request(mockit, setup_client, input_data):
    """
    Test Generator POST request - Bad Request
    """
    client = setup_client
    network = mockit('_network')

    result = client.simulate_post(path='/api/generator', json=input_data)
    assert result.status_code == 400
    assert result.json == {'title': f"Request body needs to be a dictionary with active power (`p_mw`) of the "
                                    f"generator as the key. Got {list(input_data)} instead."}

    # Assert network doesn't get called in this case at all.
    _test.assert_calls(network, [])