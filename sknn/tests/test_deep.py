import unittest
from nose.tools import (assert_is_not_none, assert_raises, assert_equal)

import io
import pickle
import numpy

from sknn.mlp import MultiLayerPerceptronRegressor as MLPR
from . import test_linear


class TestDeepNetwork(test_linear.TestLinearNetwork):

    def setUp(self):
        self.nn = MLPR(
            layers=[
                ("Rectifier", 16),
                ("Sigmoid", 12),
                ("Maxout", 8, 2),
                ("Tanh", 4),
                ("Linear",)],
            n_iter=1)

    def test_UnknownOuputActivation(self):
        nn = MLPR(layers=[("Unknown", 8)])
        a_in = numpy.zeros((8,16))
        assert_raises(NotImplementedError, nn.fit, a_in, a_in)

    def test_UnknownHiddenActivation(self):
        nn = MLPR(layers=[("Unknown", 8), ("Linear",)])
        a_in = numpy.zeros((8,16))
        assert_raises(NotImplementedError, nn.fit, a_in, a_in)

    # This class also runs all the tests from the linear network too.
