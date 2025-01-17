"""
  Дан список плиток домино в определенном порядке и положении (переворачивать нельзя)
  Необходимо найти длину самой длинной правильной цепочки
  Цепочка считается правильной, если правое число левой плитки равно левому числу правой
  Например: [(1,2),(2,3),(3,4)] - это правильная цепочка (ответ 3)
            [(2,1),(2,3),(3,4)] - это неправильная цепочка, но внутри есть правильная (ответ 2)
            [(1,1),(2,3),(3,5),(5,6),(5,5),(7,3),(3,4),(4,5),(5,6),(1,1)] - правильный ответ 4, хотя есть и цепочка длины 3
"""
import unittest


def longest_chain(chain):
    ma = 0
    k = 1
    for i in range(len(chain)-1):
        if chain[i][1] == chain[i+1][0]:
            k += 1
        else:
            k=1
        ma = max(ma,k)
    return ma


class TestChessMethods(unittest.TestCase):
    def test_p(self):
        self.assertEqual(longest_chain([(1,2),(2,3),(3,4)]),3)
        self.assertEqual(longest_chain([(2,1),(2,3),(3,4)]),2)
        self.assertEqual(longest_chain([(1,1),(2,3),(3,5),(5,6),(5,5),(7,3),(3,4),(4,5),(5,6),(1,1)]), 4)
        self.assertEqual(longest_chain([(1,1),(2,3),(3,5),(5,6),(5,5),(7,3),(3,4),(4,5),(5,6),(1,1),(1,2)]), 4)
        self.assertEqual(longest_chain([(1,1),(2,3),(3,5),(5,6),(5,5),(8,8),(7,3),(3,4),(4,5),(5,6),(1,1)]), 4)
        self.assertEqual(longest_chain([(1,1),(2,3),(3,5),(5,6),(5,5),(7,3),(13,4),(4,5),(5,6),(1,1)]), 3)
        self.assertEqual(longest_chain([]),0)


unittest.main()
