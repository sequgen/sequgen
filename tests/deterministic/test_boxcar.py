import numpy as np
from numpy.testing import assert_almost_equal

from sequgen.deterministic.boxcar import boxcar


def test_with_defaults():
    t_predict = np.arange(7)

    result = boxcar(t_predict)

    expected = np.array([0., 1., 1., 0., 0., 0., 0.])
    assert_almost_equal(result, expected)


def test_with_location():
    t_predict = np.arange(7)

    result = boxcar(t_predict, location=2)

    expected = np.array([0., 0., 1., 1., 0., 0., 0.])
    assert_almost_equal(result, expected)


def test_with_width():
    t_predict = np.arange(7)

    result = boxcar(t_predict, width=3)

    expected = np.array([0., 1., 1., 1., 1., 0., 0])
    assert_almost_equal(result, expected)


def test_with_height():
    t_predict = np.arange(7)

    result = boxcar(t_predict, height=4)

    expected = np.array([0., 4., 4., 0., 0., 0., 0])
    assert_almost_equal(result, expected)


def test_with_all_parameters():
    t_predict = np.arange(7)

    result = boxcar(t_predict, location=2, width=3, height=4)

    expected = np.array([0., 0., 4., 4., 4., 4., 0])
    assert_almost_equal(result, expected)


def test_with_negative_width():
    t_predict = np.arange(7)

    result = boxcar(t_predict, location=3, width=-1, height=5)

    expected = np.array([0., 0., 5., 5., 0., 0., 0])
    assert_almost_equal(result, expected)
