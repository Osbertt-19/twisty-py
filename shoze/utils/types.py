from enum import Enum
from typing import TYPE_CHECKING, Dict, Tuple

if TYPE_CHECKING:
    from shoze.core.cell import Cell
else:
    Cell = "Cell"


Point = Tuple[int, int]
Distances = Dict[Cell, int]
Key = Tuple[int, int]
