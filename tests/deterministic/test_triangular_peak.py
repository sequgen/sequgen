import numpy as np
from numpy.testing import assert_almost_equal

from sequgen.deterministic.triangular_peak import triangular_peak


def test_with_defaults():
    t_predict = np.arange(7)

    result = triangular_peak(t_predict, width_base_right=2)

    # TODO expected peak=1 at position 0
    expected = np.array([0.5, 0., 0., 0., 0., 0., 0.])
    assert_almost_equal(result, expected)


def test_with_placement():
    t_predict = np.arange(7)

    result = triangular_peak(t_predict, placement=3, width_base_right=2)

    # TODO expected peak=1 at position 3
    expected = np.array([0., 0., 0., 0.5, 0., 0., 0.])
    assert_almost_equal(result, expected)


def test_with_base_both_sides():
    t_predict = np.arange(7)

    result = triangular_peak(t_predict, placement=3, width_base_left=2, width_base_right=2)

    # TODO expected peak=1 at position 3
    expected = np.array([0., 0., 0., 0., 0.5, 1., 0.5])
    assert_almost_equal(result, expected)
