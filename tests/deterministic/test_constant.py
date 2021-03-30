import numpy as np
from numpy.testing import assert_almost_equal

from sequgen.deterministic.constant import constant


def test_constant():
    t_predict = np.arange(4)

    result = constant(t_predict, 10)

    expected = np.array([10, 10, 10, 10])
    assert_almost_equal(result, expected)
