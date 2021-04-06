import numpy as np
from numpy.testing import assert_almost_equal
from sequgen.deterministic.boxcar import boxcar


def test_without_height():
    t_predict = np.arange(7)

    result = boxcar(t_predict, location=1, width=1)

    expected = np.array([0., 1., 1., 0., 0., 0., 0.])
    assert_almost_equal(result, expected)


def test_with_height():
    t_predict = np.arange(7)

    result = boxcar(t_predict, location=1, width=1, height=4)

    expected = np.array([0., 4., 4., 0., 0., 0., 0])
    assert_almost_equal(result, expected)
