import sys
import unittest

sys.path.insert(0, "software")

from fusion.fusion import fuse_results


class TestFusion(unittest.TestCase):

    def test_positive_result(self):
        result = fuse_results(
            "PRESUMPTIVE POSITIVE",
            True,
            True
        )

        self.assertEqual(result, "POSITIVE")

    def test_invalid_sample(self):
        result = fuse_results(
            "PRESUMPTIVE POSITIVE",
            True,
            False
        )

        self.assertEqual(result, "INCONCLUSIVE")

    def test_disagreement(self):
        result = fuse_results(
            "PRESUMPTIVE POSITIVE",
            False,
            True
        )

        self.assertEqual(result, "INCONCLUSIVE")


if __name__ == "__main__":
    unittest.main()