import numpy


# pylint: disable=too-many-arguments
def triangular_peak(t_predict, width_base_left, width_base_right, location, height=1.0):
    """Generate a time series containing a triangular peak.

    Args:
      t_predict (Numpy array):
        Where you want the model to generate predictions.

      width_base_left (float):
        The width of the left part of the triangular peak.

      width_base_right (float):
        The width of the right part of the triangular peak.

      height (float):
        The height of the peak.

      location (float):
        Where the peak should be placed on the time axis.

    Returns:
      Numpy array of shape equal to t_predict containing the curve for a triangular peak.
    """

    widths = [0, width_base_left, width_base_right]
    y = [0, height, 0]

    t = location - width_base_left + numpy.cumsum(widths)

    return numpy.interp(t_predict, t, y)
