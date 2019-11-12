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
        data = req.media
        try:
            p_mw = float(data['p_mw'])
            q_mvar = float(data['q_mvar'])
        except (KeyError, ValueError, TypeError):
            raise _falcon.HTTPBadRequest(f"Request body needs to be a dictionary with active power (`p_mw`) and "
                                         f"reactive power (`q_mvar`) of the load as the key. Got {data} instead.")
        _network.net.set_load_params(p_mw, q_mvar)
        resp.status = _falcon.HTTP_200


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
        data = req.media
        try:
            p_mw = float(data['p_mw'])
        except (KeyError, ValueError, TypeError):
            raise _falcon.HTTPBadRequest(f"Request body needs to be a dictionary with active power (`p_mw`) of the "
                                         f"generator as the key. Got {data} instead.")
        _network.net.set_generator_params(p_mw)
        resp.status = _falcon.HTTP_200
