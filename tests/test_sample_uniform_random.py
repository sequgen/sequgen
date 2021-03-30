import numpy as np
import pytest
from numpy.testing import assert_almost_equal

from sequgen.samplers.sample_uniform_random import sample_uniform_random


@pytest.fixture
def random_seeded():
    np.random.seed(42)


def test_with_lists(random_seeded):
    result = sample_uniform_random(['somename'],
                                   [-10],
                                   [10])

    expected = np.array([-2.5091976])
    assert_almost_equal(result['somename'], expected)


def test_with_array(random_seeded):
    result = sample_uniform_random(np.array(['somename']),
                                   np.array([-10]),
                                   np.array([10]))

    expected = np.array([-2.5091976])
    assert_almost_equal(result['somename'], expected)


def test_with_2dimensions(random_seeded):
    result = sample_uniform_random(['x', 'y'],
                                   [-10, 2],
                                   [10, 4])

    assert result.keys() == {'x', 'y'}
    assert_almost_equal(result['x'], np.array([-2.5091976]))
    assert_almost_equal(result['y'], np.array([3.9014286]))
