import numpy as np
from numpy.testing import assert_almost_equal

from sequgen.deterministic.sine import sine


def test_with_defaults():
    t_predict = np.linspace(0, 1, 20)

    wavelength = 1.0
    result = sine(t_predict, wavelength)

    expected = np.array([0.00000000e+00, 3.24699469e-01, 6.14212713e-01, 8.37166478e-01,
                         9.69400266e-01, 9.96584493e-01, 9.15773327e-01, 7.35723911e-01,
                         4.75947393e-01, 1.64594590e-01, -1.64594590e-01, -4.75947393e-01,
                         -7.35723911e-01, -9.15773327e-01, -9.96584493e-01, -9.69400266e-01,
                         -8.37166478e-01, -6.14212713e-01, -3.24699469e-01, -2.44929360e-16, ]
                        )
    assert_almost_equal(result, expected)
