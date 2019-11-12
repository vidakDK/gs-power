"""
Utility functions for testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


def assert_calls(value, expected, sort=False):
    """ Assert mock_calls """
    result = calls(value)
    if sort:
        result.sort()
    assert result == expected, result


def calls(value):
    """ Map calls to list of tuples """
    return list(map(tuple, value.mock_calls))