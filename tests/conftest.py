import numpy as np
import pytest


@pytest.fixture
def random_seeded():
    np.random.seed(42)
