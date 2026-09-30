import unittest
import math

from vector import vector


class TestVec(unittest.TestCase):

    def test_mean(self):
        v = vector([2, 4, 6, 8])

        self.assertEqual(v.mean(), 5)

    def test_mean_between_min_and_max(self):
        v = vector([2, 4, 6, 8])

        self.assertGreaterEqual(v.mean(), min(v.elements))
        self.assertLessEqual(v.mean(), max(v.elements))

    def test_demean(self):
        v = vector([2, 4, 6, 8])

        result = v.demean()

        expected = vector([-3, -1, 1, 3])

        self.assertEqual(result.elements, expected.elements)

    def test_demean_mean_is_zero(self):
        v = vector([2, 4, 6, 8])

        result = v.demean()

        self.assertAlmostEqual(result.mean(), 0.0)

    def test_demean_does_not_change_original(self):
        v = vector([2, 4, 6, 8])

        original = v.elements

        result = v.demean()

        self.assertEqual(v.elements, original)
        self.assertIsNot(v, result)

    def test_std(self):
        v = vector([2, 4, 6, 8])

        self.assertAlmostEqual(v.std(), math.sqrt(5))

    def test_std_non_negative(self):
        v = vector([2, 4, 6, 8])

        self.assertGreaterEqual(v.std(), 0)

    def test_std_constant_vector(self):
        v = vector([5, 5, 5, 5])

        self.assertEqual(v.std(), 0)

    def test_demean_constant_vector(self):
        v = vector([5, 5, 5, 5])

        result = v.demean()

        self.assertEqual(result.elements, (0, 0, 0, 0))

    def test_std_single_value(self):
        v = vector([10])

        self.assertEqual(v.std(), 0)


if __name__ == "__main__":
    unittest.main()