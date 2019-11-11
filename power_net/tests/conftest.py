"""
Fixtures for Pytest
~~~~~~~~~~~~~~~~~~~
"""

import typing as _typing

import pytest as _pytest


@_pytest.fixture
def mockit(request, mocker):
    def proxy(target, module=None):
        if module is None:
            module = request.module.MOCKIT
        return mocker.patch(module.__name__ + '.' + target)
    return proxy


@_pytest.fixture
def patch_constants(monkeypatch):
    def inner(module_name: str, constants: _typing.Dict[str, _typing.Any]):
        for key, value in constants.items():
            monkeypatch.setattr(f"{module_name}.{key}", value)
    return inner
