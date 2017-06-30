"""
Test if the run are repeatable, i.e., successive runs yield the same results, given a fixed
random seed.
"""

import unittest
import numpy as np
import array

import dotdot
from neuromodel import Model, MatlabModel


class RepeatableTests(unittest.TestCase):
    """Test repeatability"""

    def test_repeatable(self):
        """Test that two 50-steps runs yield the same history"""

        def run(seed, ModelClass=Model):
            """Return the history of a run"""
            model = ModelClass(range_A=[0, 20], range_B=[0, 20], random_seed=seed)
            return model.one_trial(1, 10)

        self.assertEqual(run(0, ModelClass=Model), run(0, ModelClass=Model))
        self.assertEqual(run(0, ModelClass=MatlabModel), run(0, ModelClass=MatlabModel))


if __name__ == '__main__':
    unittest.main()
