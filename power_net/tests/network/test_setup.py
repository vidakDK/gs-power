"""
Test power network setup methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import json as _json

import pytest as _pytest

from power_net.app.network import setup as _setup
from power_net.tests import _util as _test

MOCKIT = _setup


@_pytest.fixture()
def setup_network():
    net = _setup.PowerNetwork()
    return net


def test_get_generator_res(setup_network):
    """ Test get_generator_res """
    net = setup_network
    expected_result = '{"p_mw":{"0":0.2},"q_mvar":{"0":0.0}}'
    result = net.get_generator_res()
    assert result == expected_result


def test_get_load_res(setup_network):
    """ Test get_load_res """
    net = setup_network
    expected_result = '{"p_mw":{"0":0.1},"q_mvar":{"0":0.05}}'
    result = net.get_load_res()
    assert result == expected_result


def test_set_load_params(mockit, setup_network):
    net = setup_network
    pp = mockit('_pp')
    p_mw = 0.4
    q_mvar = 0.1
    net.set_load_params(p_mw, q_mvar)

    assert net._net.load['p_mw'][0] == p_mw
    assert net._net.load['q_mvar'][0] == q_mvar
    _test.assert_calls(pp, [('runpp', (net._net,), {})])


def test_set_generator_params(mockit, setup_network):
    net = setup_network
    pp = mockit('_pp')
    p_mw = 0.4
    net.set_generator_params(p_mw)

    assert net._net.sgen['p_mw'][0] == p_mw
    _test.assert_calls(pp, [('runpp', (net._net,), {})])
