import numpy as np
from numpy.testing import assert_almost_equal
from sequgen.deterministic.triangular_peak import triangular_peak


def test_with_required_args():
    t_predict = np.linspace(0, 5, 11)
    result = triangular_peak(t_predict, width_base_left=1.0, width_base_right=1.0, location=1.0)
    expected = np.array([0, 0.5, 1.0, 0.5, 0., 0., 0., 0., 0., 0., 0.])
    assert_almost_equal(result, expected)


def test_with_required_args_and_height():
    t_predict = np.linspace(0, 5, 11)
    result = triangular_peak(t_predict, width_base_left=1.0, width_base_right=1.0, location=1.0, height=2.0)
    expected = np.array([0, 1.0, 2.0, 1.0, 0., 0., 0., 0., 0., 0., 0.])
    assert_almost_equal(result, expected)


def test_with_required_args_and_skewness():
    t_predict = np.linspace(0, 5, 11)
    result = triangular_peak(t_predict, width_base_left=1.0, width_base_right=2.0, location=1.0)
    expected = np.array([0, 0.5, 1.0, 0.75, 0.5, 0.25, 0., 0., 0., 0., 0.])
    assert_almost_equal(result, expected)
