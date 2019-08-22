import unittest

from WordRPG.engine.common import Point, Table



def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)


pos1 = Point(1,10)
col, row = pos1
print(f"col:{col}, row:{row}")
print(f"col:{pos1.col}, row:{pos1.row}")
print(f"col:{pos1[0]}, row:{pos1[1]}")

print(f'print : {pos1}')
print(f'repr : {repr(pos1)}')


pos2 = Point(50,100)

print(pos1)
print(pos2)

print(pos1 + pos2)
print(pos1 + pos2)
print(pos1 * pos2)

# array = [list(range(0,10)),
#          list(range(11,20)),
#          list(range(21,30)),
#         ]
# test_grid = Table(array)

# print(f"rerp : {repr(test_grid)}")
# print(f"string : {test_grid}")
# print(f"length : {len(test_grid)}")
# print(test_grid[0][1])


# print(type(test_grid))
# print(test_grid.cells)
# print(test_grid.cells[0][1])  # gets [row][col] in cells
# print(test_grid.get((0,1)))   # gets (col,row) in cells
# print(test_grid)
# print(len(test_grid[0]))
# print(test_grid)