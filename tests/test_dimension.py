import pytest

from sequgen.dimension import Dimension


class TestDimensionWithUpperBound:
    @pytest.fixture
    def dimension(self):
        return Dimension('somename', -10, 10)

    def test_name(self, dimension: Dimension):
        assert dimension.name == 'somename'

    def test_lower_bound(self, dimension: Dimension):
        assert dimension.lower_bound == -10

    def test_upper_bound(self, dimension: Dimension):
        assert dimension.upper_bound == 10


class TestDimensionWithoutUpperBound:
    @pytest.fixture
    def dimension(self):
        return Dimension('somename', -10)

    def test_name(self, dimension: Dimension):
        assert dimension.name == 'somename'

    def test_lower_bound(self, dimension: Dimension):
        assert dimension.lower_bound == -10

    def test_upper_bound(self, dimension: Dimension):
        assert dimension.upper_bound == -10
