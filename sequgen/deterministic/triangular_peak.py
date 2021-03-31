import numpy


# pylint: disable=too-many-arguments
def triangular_peak(t_predict, width_leading=None, width_base_left=None, width_base_right=None, width_trailing=None,
                    width=1.0, height=1.0, location=0, sign=1):
    """Generate a time series containing a triangular peak.

    Args:
      t_predict (Numpy array):
        Where you want the model to generate predictions.

      width_leading (float):
        The width of the leading part of the triangular peak, i.e. the part before the peak starts to climb.

      width_base_left (float):
        The width of the left part of the triangular peak.

      width_base_right (float):
        The width of the right part of the triangular peak.

      width_trailing (float):
        The width of the trailing part of the triangular peak, i.e. the part after the peak returns back to
        the baseline.

      width (float):
        The width of entire peak (excluding any leading and trailing parts).

      height (float):
        The height of the peak.

      location (float):
        Where the peak should be placed on the time axis.

      sign (float):
        Whether the peak should be right side up or upside down.

        """

    assert sign in [-1, 1], "sign should be -1 or 1"

    if width is None:
        assert width_base_left is not None
        assert width_base_right is not None

    if width_base_left is None:
        assert width is not None
        assert width_base_right is not None
        width_base_left = width - width_base_right

    if width_base_right is None:
        assert width is not None
        assert width_base_left is not None
        width_base_right = width - width_base_left

    widths = [0, width_leading, width_base_left, width_base_right, width_trailing]
    y = [0, 0, height, 0, 0]

    if width_leading is None:
        widths.pop(1)
        y.pop(1)

    if width_trailing is None:
        widths.pop(-1)
        y.pop(-1)

    t = location + numpy.cumsum(widths)

    return sign * numpy.interp(t_predict, t, y)
