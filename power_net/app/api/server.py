""" Falcon API """

import falcon as _falcon

from . import _resources


def _create_api():
    """
    Create Falcon API client
    """
    app = _falcon.API()
    app.add_route('/api/load', _resources.LoadResource())
    app.add_route('/api/generator', _resources.GeneratorResource())

    return app


app = _create_api()
