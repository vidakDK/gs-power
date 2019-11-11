"""
Power network setup
~~~~~~~~~~~~~~~~~~~
"""

import pandapower as _pp


class PowerNetwork:
    def __init__(self):
        # create empty net
        net = _pp.create_empty_network()

        # create buses
        b1 = _pp.create_bus(net, vn_kv=20., name="Bus 1")
        b2 = _pp.create_bus(net, vn_kv=0.4, name="Bus 2")
        b3 = _pp.create_bus(net, vn_kv=0.4, name="Bus 3")

        # create bus elements
        _pp.create_ext_grid(net, bus=b1, vm_pu=1.02, name="Grid Connection")
        _pp.create_sgen(net, bus=b3, p_mw=0.2, name="Generator"),
        _pp.create_load(net, bus=b3, p_mw=0.1, q_mvar=0.05, name="Load")

        # create branch elements
        trafo = _pp.create_transformer(net, hv_bus=b1, lv_bus=b2, std_type="0.4 MVA 20/0.4 kV", name="Trafo")
        line = _pp.create_line(net, from_bus=b2, to_bus=b3, length_km=0.1, name="Line", std_type="NAYY 4x50 SE")

        # run power flow:
        _pp.runpp(net)

        # assign variable
        self._net = net

    def get_load_res(self) -> str:
        return self._net.res_load.to_json()

    def get_generator_res(self) -> str:
        return self._net.res_sgen.to_json()


# Initialize at import level given that the network is static and we run the power flow once.
net = PowerNetwork()
