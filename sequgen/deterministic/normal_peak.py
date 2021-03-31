import numpy


def normal_peak(t_predict, location=0.0, stddev=1.0, height=1.0):
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

    Returns:
      Numpy array with shape equal to t_predict, containing the y values for the normal peak curve.
    """

    max_height = 1 / (stddev * numpy.sqrt(2 * numpy.pi))
    z = (t_predict - location) / stddev
    term1 = 1 / (stddev * numpy.sqrt(2 * numpy.pi))
    term2 = numpy.exp((-1 / 2) * numpy.power(z, 2))
    return height * term1 * term2 / max_height
