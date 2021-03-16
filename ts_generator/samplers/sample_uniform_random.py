import numpy


def sample_uniform_random(dimension_names=None, lower_bounds=None, upper_bounds=None):

    n_dims = len(dimension_names)
    sample = lower_bounds + numpy.random.rand(n_dims) * (upper_bounds - lower_bounds)

    return {item[0]: item[1] for item in zip(dimension_names, sample)}
