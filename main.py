import warnings
from shoze.core.cell import Cell


cell = Cell(1, 2)
with warnings.catch_warnings(record=True) as w:
    cell.unlink(Cell(4, 5))
    print(len(w))
    print(w[0].message)
