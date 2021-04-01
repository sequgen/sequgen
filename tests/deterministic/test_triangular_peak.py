import numpy as np
from numpy.testing import assert_almost_equal
from sequgen.deterministic.triangular_peak import triangular_peak


def test_with_required_args():
    t_predict = np.linspace(0, 5, 11)
    actual = triangular_peak(t_predict, width_base_left=1.0, width_base_right=1.0, location=1.0)
    expected = np.array([0, 0.5, 1.0, 0.5, 0., 0., 0., 0., 0., 0., 0.])
    assert_almost_equal(actual, expected)


def test_with_required_args_and_height():
    t_predict = np.linspace(0, 5, 11)
    actual = triangular_peak(t_predict, width_base_left=1.0, width_base_right=1.0, location=1.0, height=2.0)
    expected = np.array([0, 1.0, 2.0, 1.0, 0., 0., 0., 0., 0., 0., 0.])
    assert_almost_equal(actual, expected)


def test_with_required_args_and_skewness():
    t_predict = np.linspace(0, 5, 11)
    location = 1.0
    actual = triangular_peak(t_predict, width_base_left=1.0, width_base_right=2.0, location=location)
    expected = np.array([0, 0.5, 1.0, 0.75, 0.5, 0.25, 0., 0., 0., 0., 0.])
    default_height = 1.0
    assert actual[t_predict == location] == default_height, "expected maximum height at t == location"
    assert_almost_equal(actual, expected)

def test_with_zero_base_left():
    t_predict = np.linspace(0, 5, 11)  # array([0. , 0.5, 1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5, 5. ])
    actual = triangular_peak(t_predict, width_base_left=0.0, width_base_right=2.0, location=1.0)
    expected = np.array([])
    assert_almost_equal(actual, expected)

def test_with_zero_base_right():
    t_predict = np.linspace(0, 5, 11)
    actual = triangular_peak(t_predict, width_base_left=2.0, width_base_right=0.0, location=3.0)
    expected = np.array([])
    assert_almost_equal(actual, expected)
