""" API endpoints """

import falcon as _falcon

from . import _network


class LoadResource:
    """ Resource for Load endpoints """
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = _falcon.HTTP_200
        resp.body = _network.net.get_load_res()


class GeneratorResource:
    """ Resource for Generator endpoints """
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = _falcon.HTTP_200
        resp.body = _network.net.get_generator_res()
