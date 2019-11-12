"""
API endpoints
~~~~~~~~~~~~~
"""

import falcon as _falcon

from .. import network as _network


class LoadResource:
    """
    Resource for Load endpoints
    """

    def on_get(self, req: _falcon.Request, resp: _falcon.Response):
        """
        Handle GET requests
        """
        resp.status = _falcon.HTTP_200
        resp.body = _network.net.get_load_res()

    def on_post(self, req: _falcon.Request, resp: _falcon.Response):
        """
        Handle POST requests
        """
        raise NotImplementedError("This feature is yet to be implemented :D")


class GeneratorResource:
    """
    Resource for Generator endpoints
    """

    def on_get(self, req: _falcon.Request, resp: _falcon.Response):
        """
        Handle GET requests
        """
        resp.status = _falcon.HTTP_200
        resp.body = _network.net.get_generator_res()

    def on_post(self, req: _falcon.Request, resp: _falcon.Response):
        """
        Handle POST requests
        """
        raise NotImplementedError("This feature is yet to be implemented :D")
