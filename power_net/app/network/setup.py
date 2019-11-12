"""
Power network setup
~~~~~~~~~~~~~~~~~~~
"""

import pandapower as _pp


class PowerNetwork:
    """
    Power Network setup and methods for calculating power flow and serving the
    results.
    """
    def __init__(self):
        """
        Initialize the network and run power flow.
        """

        # create empty net
        net = _pp.create_empty_network()

        # create buses
        bus1 = _pp.create_bus(net, vn_kv=20., name="Bus 1")
        bus2 = _pp.create_bus(net, vn_kv=0.4, name="Bus 2")
        bus3 = _pp.create_bus(net, vn_kv=0.4, name="Bus 3")

        # create bus elements
        _pp.create_ext_grid(net, bus=bus1, vm_pu=1.02, name="Grid Connection")
        _pp.create_sgen(net, bus=bus3, p_mw=0.2, name="Generator")
        _pp.create_load(net, bus=bus3, p_mw=0.1, q_mvar=0.05, name="Load")

        # create branch elements
        _pp.create_transformer(net, hv_bus=bus1, lv_bus=bus2, std_type="0.4 MVA 20/0.4 kV", name="Trafo")
        _pp.create_line(net, from_bus=bus2, to_bus=bus3, length_km=0.1, name="Line", std_type="NAYY 4x50 SE")

        # run power flow:
        _pp.runpp(net)

        # assign variable
        self._net = net

    def get_load_res(self) -> str:
        """
        Get the results of the power flow for the load resource.

        Returns:
            json representation of the result
        """
        return self._net.res_load.to_json()

    def get_generator_res(self) -> str:
        """
        Get the results of the power flow for the generator resource.

        Returns:
            json representation of the result
        """
        return self._net.res_sgen.to_json()

    def set_load_params(self, p_mw: float, q_mvar: float) -> None:
        """
        Set parameters for the load element in the network and re-run the power flow.

        Args:
            p_mw: active power
            q_mvar: reactive power
        """
        self._net.load.p_mw = p_mw
        self._net.load.q_mvar = q_mvar
        _pp.runpp(self._net)

    def set_generator_params(self, p_mw: float) -> None:
        """
        Set parameters for the generator element in the network and re-run the power flow.

        Args:
            p_mw: active power
        """
        self._net.sgen.p_mw = p_mw
        _pp.runpp(self._net)


# Initialize at import level given that the network is static and we run the power flow at initialization.
net = PowerNetwork()
