"""
Project utility module.

Contains pint for physical unit conversion and handling, as well as the binary compiled
cm_infofiles.
"""
from pint import UnitRegistry

ureg = UnitRegistry()
Q_ = ureg.Quantity
