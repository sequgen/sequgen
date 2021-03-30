import numpy as np
from numpy.testing import assert_almost_equal

from sequgen.deterministic.normal_peak import normal_peak


def test_with_defaults():
    t_predict = np.arange(15)

    result = normal_peak(t_predict)

    expected = np.array([1.0000000e+00, 6.0653066e-01, 1.3533528e-01, 1.1108997e-02,
                         3.3546263e-04, 3.7266532e-06, 1.5229980e-08, 2.2897348e-11,
                         1.2664166e-14, 2.5767571e-18, 1.9287498e-22, 5.3110922e-27,
                         5.3801862e-32, 2.0050088e-37, 2.7487850e-43])
    assert_almost_equal(result, expected)
