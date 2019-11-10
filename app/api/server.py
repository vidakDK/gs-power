""" Falcon API """

import falcon as _falcon

from . import _resources

app = _falcon.API()
app.add_route('/load', _resources.LoadResource())
app.add_route('/generator', _resources.GeneratorResource())
