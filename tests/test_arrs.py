import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_get_non_existing_index(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(arrs.get(array, 10, default=0), 0)

    def test_get_negative_index(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(arrs.get(array, -1), None)

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -1, 2), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], -5, 1), [1])
        self.assertEqual(arrs.my_slice([]), [])

    def test_my_slice_with_start(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(arrs.my_slice(array, start=2), [3, 4, 5])

    def test_my_slice_with_end(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(arrs.my_slice(array, end=3), [1, 2, 3])

    def test_my_slice_with_start_and_end(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(arrs.my_slice(array, start=1, end=4), [2, 3, 4])

    def test_my_slice_with_negative_start_and_end(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(arrs.my_slice(array, start=-3, end=-1), [3, 4])

    def test_my_slice_with_out_of_bounds_indexes(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(arrs.my_slice(array, start=10), [])
        self.assertEqual(arrs.my_slice(array, end=10), [1, 2, 3, 4, 5])