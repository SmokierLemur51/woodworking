from .cost import update_cost
from .finances import finances
from .gui.qtgui import run

ARGUMENTS = {
    "finances": finances,
    "gui": run,
    "updatecost": update_cost, 
}