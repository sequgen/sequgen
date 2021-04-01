import numpy


# pylint: disable=too-many-arguments
def triangular_peak(t_predict, width_base_left, width_base_right, location, height=1.0):
    """Generate a time series containing a triangular peak.

    Args:
      t_predict (Numpy array):
        Where you want the model to generate predictions.

      width_base_left (float):
        The width of the left part of the triangular peak in units of t_predict.

      width_base_right (float):
        The width of the right part of the triangular peak in units of t_predict.

      height (float):
        The height of the peak in user-defined units.

      location (float):
        Where the peak should be placed on the time axis in units of t_predict.

    Returns:
      Numpy array of shape equal to t_predict containing the curve for a triangular peak in user-defined units.
    """

    assert width_base_left > 0, "width_base_left should be > 0"
    assert width_base_right > 0, "width_base_right should be > 0"

    widths = [0, width_base_left, width_base_right]
    y = [0, height, 0]

    t = location - width_base_left + numpy.cumsum(widths)

    return numpy.interp(t_predict, t, y)
