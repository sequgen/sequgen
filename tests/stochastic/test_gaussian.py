import numpy as np
from numpy.testing import assert_almost_equal

from sequgen.stochastic.gaussian import gaussian


def test_gaussian_with_defaults(random_seeded):
    t_predict = np.arange(4)

    result = gaussian(t_predict)

    expected = np.array([0.4967142, -0.1382643,  0.6476885,  1.5230299])
    assert_almost_equal(result, expected)


def test_gaussian_with_correlationlength2(random_seeded):
    t_predict = np.arange(4)

    result = gaussian(t_predict, stddev=2, average=-5, correlation_length=2)

    expected = np.array([-4.0065717, -4.6415501, -4.1730865, -3.0635134])
    assert_almost_equal(result, expected)
