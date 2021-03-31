import numpy


def normal_peak(t_predict, location=0.0, stddev=1.0, unit_integral=None, height=None):
    """Generates a peak whose shape is the gaussian distribution function
    Args:
      t_predict:
        Numpy array with points in time where you want the model to generate predictions.
      location (float):
        Where you want to place the peak of the curve.
      stddev (float):
        Shape factor that affects the width of the distribution.
      height (float):
        What the peak height should be.
      unit_integral (bool):
        If true, area under the curve sums to unity

    Returns:
      Numpy array with shape equal to t_predict, containing the y values for the normal peak curve.
    """

    if unit_integral is None:
        # pylint: disable=simplifiable-if-statement
        if height is None:
            # user did not specify unit_integral or height
            unit_integral = True
        else:
            # user specified height
            unit_integral = False
    elif unit_integral is False:
        assert height is not None, "You need to specifiy height when unit_integral is False."
    elif unit_integral is True:
        assert height is None, "Either define height or set unit_integral to True, but not both."
    else:
        raise AssertionError("unit_integral should be None, True, or False")

    # determine scaling parameter
    if unit_integral is True:
        scale = 1.0
    elif unit_integral is False:
        max_height = 1 / (stddev * numpy.sqrt(2 * numpy.pi))
        scale = height / max_height
    else:
        raise AssertionError("expected unit_integral to be True, False, or None")

    z = (t_predict - location) / stddev
    term1 = 1 / (stddev * numpy.sqrt(2 * numpy.pi))
    term2 = numpy.exp((-1 / 2) * numpy.power(z, 2))
    return term1 * term2 * scale
