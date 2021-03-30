import numpy as np
from numpy.testing import assert_almost_equal

from sequgen.deterministic.sine import sine


def test_with_defaults():
    t_predict = np.arange(15)

    result = sine(t_predict)

    expected = np.array([0.0000000e+00, -2.4492936e-16, -4.8985872e-16, -7.3478808e-16,
                         -9.7971744e-16, -1.2246468e-15, -1.4695762e-15, -1.7145055e-15,
                         -1.9594349e-15, -2.2043642e-15, -2.4492936e-15, -9.7996503e-15,
                         -2.9391523e-15, 3.9213457e-15, -3.4290110e-15])
    assert_almost_equal(result, expected)
