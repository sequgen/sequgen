import numpy as np
from numpy.testing import assert_almost_equal
import pytest
from sequgen.deterministic.triangular_peak import triangular_peak


"""
In the test names below, the t and f represents whether the user has defined arguments
width, width_base_left, width_base_right, height (in that order)
"""


def test_with_fttf_and_location():
    t_predict = np.linspace(0, 5, 11)
    opts = dict(width=None,
                width_base_left=1.0,
                width_base_right=1.0,
                height=None)
    actual = triangular_peak(t_predict, **opts, location=1.0, unit_integral=True)
    expected = np.array([0, 0.5, 1.0, 0.5, 0., 0., 0., 0., 0., 0., 0.])
    assert_almost_equal(actual, expected)


def test_with_fttt_and_location():
    t_predict = np.linspace(0, 5, 11)
    opts = dict(width=None,
                width_base_left=1.0,
                width_base_right=1.0,
                height=1.0)
    actual = triangular_peak(t_predict, **opts, location=1.0, unit_integral=True)
    expected = np.array([0, 0.5, 1.0, 0.5, 0., 0., 0., 0., 0., 0., 0.])
    assert_almost_equal(actual, expected)


def test_with_fttf_with_skewness_and_location():
    t_predict = np.linspace(0, 5, 11)
    location = 1.0
    opts = dict(width=None,
                width_base_left=1.0,
                width_base_right=2.0,
                height=None)
    actual = triangular_peak(t_predict, **opts, location=location, unit_integral=True)
    expected = np.array([0, 1/3, 2/3, 1/2, 1/3, 1/6, 0., 0., 0., 0., 0.])
    assert_almost_equal(actual, expected)


def test_with_fttf_small_base_left_irregular_sampling():
    t_predict = np.asarray([0, 1-1e-9, 1, 2, 3, 10])
    opts = dict(width=None,
                width_base_left=1e-9,
                width_base_right=2.0,
                height=None)
    actual = triangular_peak(t_predict, **opts, location=1.0, unit_integral=True)
    expected = np.array([0., 0., 1., 0.50, 0., 0.])
    assert_almost_equal(actual, expected)


def test_with_fttf_small_base_left_regular_sampling():
    t_predict = np.linspace(0, 5, 11)
    opts = dict(width=None,
                width_base_left=1e-9,
                width_base_right=2.0,
                height=None)
    actual = triangular_peak(t_predict, **opts, location=1.0, unit_integral=True)
    expected = np.array([0., 0., 1., 0.75, 0.50, 0.25, 0., 0., 0., 0., 0.])
    assert_almost_equal(actual, expected)


def test_with_fttf_small_base_right_irregular_sampling():
    t_predict = np.asarray([0, 1.0, 2.0, 3.0, 3+1e-9, 10])
    opts = dict(width=None,
                width_base_left=2.0,
                width_base_right=1e-9,
                height=None)
    actual = triangular_peak(t_predict, **opts, location=3.0, unit_integral=True)
    expected = np.array([0., 0., 0.50, 1.0, 0., 0.])
    assert_almost_equal(actual, expected)


def test_with_fttf_small_base_right_regular_sampling():
    t_predict = np.linspace(0, 5, 11)
    opts = dict(width=None,
                width_base_left=2.0,
                width_base_right=1e-9,
                height=None)
    actual = triangular_peak(t_predict, **opts, location=3.0, unit_integral=True)
    expected = np.array([0., 0., 0., 0.25, 0.50, 0.75, 1.0, 0., 0., 0., 0.])
    assert_almost_equal(actual, expected)


def test_with_tfff_and_location():
    t_predict = np.linspace(0, 5, 11)
    opts = dict(width=2.0,
                width_base_left=None,
                width_base_right=None,
                height=None)
    actual = triangular_peak(t_predict, **opts, location=1.0, unit_integral=True)
    expected = np.array([0, 0.5, 1.0, 0.5, 0., 0., 0., 0., 0., 0., 0.])
    assert_almost_equal(actual, expected)


def test_with_fttf_zero_base_left():
    t_predict = np.linspace(0, 5, 11)
    opts = dict(width=None,
                width_base_left=0.0,
                width_base_right=2.0,
                height=None)
    with pytest.raises(AssertionError) as excinfo:
        triangular_peak(t_predict, **opts, location=1.0, unit_integral=True)
    assert "width_base_left should be > 0" in str(excinfo.value)


def test_with_fttf_zero_base_right_regular_sampling():
    t_predict = np.linspace(0, 5, 11)
    opts = dict(width=None,
                width_base_left=2.0,
                width_base_right=0.0,
                height=None)
    with pytest.raises(AssertionError) as excinfo:
        triangular_peak(t_predict, **opts, location=3.0, unit_integral=True)
    assert "width_base_right should be > 0" in str(excinfo.value)
