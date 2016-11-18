import unittest
from SmallestEnclosingCircle import make_smallest_circle

class TestSmallestEnclosingCircle(unittest.TestCase):
  def test_make_smallest_circle(self):
    self.assertEqual(make_smallest_circle(((0,0), (2,0))), (1, 0, 1))
    self.assertEqual(make_smallest_circle(((0,0), (1,0), (2,0))), (1, 0, 1))
    self.assertEqual(make_smallest_circle(((0,1),(1,0),(-1,0))), (0, 0, 1))

    self.assertEqual(make_smallest_circle(((0,0),)), (0,0,0))
    self.assertEqual(make_smallest_circle(((0,0),(0,0))), (0,0,0))

    self.assertEqual(make_smallest_circle(((-1,0),(1,0),(0,2),(0,-2))), (0,0,2))



if __name__ == '__main__': unittest.main()
