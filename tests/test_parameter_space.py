import numpy as np
import pytest
from numpy.testing import assert_almost_equal
from sequgen.dimension import Dimension
from sequgen.parameter_space import ParameterSpace
from sequgen.samplers.sample_uniform_random import sample_uniform_random


class TestParameterSpaceWithSinglePlainDimension:
    @pytest.fixture
    def space(self, random_seeded):
        return ParameterSpace(
            [Dimension('somename', -10, 10)],
            sample_uniform_random
        )

    def test_repr(self, space: ParameterSpace):
        expected = "1-D parameter space with dimensions: 'somename'"
        assert repr(space) == expected

    def test_format_str(self, space: ParameterSpace):
        expected = 'somename={somename:.2f}'
        assert space.format_str() == expected

    def test_sample(self, space: ParameterSpace):
        result = space.sample()

        assert result.keys() == {'somename'}
        assert_almost_equal(result['somename'], np.array([-2.5091976]))


def test_default_sampler(random_seeded):
    space = ParameterSpace([Dimension('somename', -10, 10)])

    assert space.sampler == sample_uniform_random
