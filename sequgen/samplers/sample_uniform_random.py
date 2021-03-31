import numpy


def sample_uniform_random(dimension_names=None, lower_bounds=None, upper_bounds=None):
    """Takes a uniform random sample from the parameter space.

    Args:
      dimension_names:
        Array of names of the dimensions of the parameter space.
      lower_bounds:
        Array of lower bounds of the dimensions of the parameter space.
      upper_bounds:
        Array of upper bounds of the dimensions of the parameter space.

    Returns:
        Dictionary with keys equal to the dimension names, together representing a uniform random draw
        from the parameter space.
    """

    if isinstance(dimension_names, list):
        dimension_names = numpy.asarray(dimension_names)

    if isinstance(lower_bounds, list):
        lower_bounds = numpy.asarray(lower_bounds)

    if isinstance(upper_bounds, list):
        upper_bounds = numpy.asarray(upper_bounds)

    n_dims = len(dimension_names)
    sample = lower_bounds + numpy.random.rand(n_dims) * (upper_bounds - lower_bounds)

    return {item[0]: item[1] for item in zip(dimension_names, sample)}
