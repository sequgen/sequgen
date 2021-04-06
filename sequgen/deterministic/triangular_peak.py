import numpy


# pylint: disable=too-many-arguments,too-many-locals
def triangular_peak(t_predict, location, width=None, width_base_left=None, width_base_right=None, height=None):
    """Generate a time series containing a triangular peak.

    Args:
      t_predict (Numpy array):
        Where you want the model to generate predictions.

      width (float):
        The overall width of the triangular peak in units of t_predict.

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

    def derive_unit_height():
        return width, width_base_left, width_base_right, 1.0

    def derive_width():
        assert width_base_left > 0, "width_base_left should be > 0"
        assert width_base_right > 0, "width_base_right should be > 0"
        _width = width_base_left + width_base_right
        return _width, width_base_left, width_base_right, height

    def derive_width_and_unit_height():
        _width, _, _, _ = derive_width()
        return _width, width_base_left, width_base_right, 1.0

    def derive_width_base_left():
        assert width > 0, "width should be > 0"
        assert width_base_right > 0, "width_base_right should be > 0"
        _width_base_left = width - width_base_right
        return width, _width_base_left, width_base_right, height

    def derive_width_base_left_and_right():
        assert width > 0, "width should be > 0"
        _width_base_left = width / 2
        _width_base_right = width / 2
        return width, _width_base_left, _width_base_right, height

    def derive_width_base_left_and_right_and_unit_height():
        _, _width_base_left, _width_base_right, _ = derive_width_base_left_and_right()
        return width, _width_base_left, _width_base_right, 1.0

    def derive_width_base_left_and_unit_height():
        _, _width_base_left, _, _ = derive_width_base_left()
        return width, _width_base_left, width_base_right, 1.0

    def derive_width_base_right():
        assert width > 0, "width should be > 0"
        assert width_base_left > 0, "width_base_left should be > 0"
        _width_base_right = width - width_base_left
        return width, width_base_left, _width_base_right, height

    def derive_width_base_right_and_unit_height():
        _, _, _width_base_right, _ = derive_width_base_right()
        return width, width_base_left, _width_base_right, 1.0

    def verify_consistency():
        assert width_base_left > 0, "width_base_left should be > 0"
        assert width_base_right > 0, "width_base_right should be > 0"
        assert width_base_right + width_base_left == width
        return width, width_base_left, width_base_right, height

    def raise_error():
        raise AssertionError("Behavior is not defined for the given combination of inputs.")

    behavior = {
        (True, True, True, True): verify_consistency,
        (True, True, True, False): derive_unit_height,
        (True, True, False, True): derive_width_base_right,
        (True, True, False, False): derive_width_base_right_and_unit_height,
        (True, False, True, True): derive_width_base_left,
        (True, False, True, False): derive_width_base_left_and_unit_height,
        (True, False, False, True): derive_width_base_left_and_right,
        (True, False, False, False): derive_width_base_left_and_right_and_unit_height,
        (False, True, True, True): derive_width,
        (False, True, True, False): derive_width_and_unit_height,
        (False, True, False, True): raise_error,
        (False, True, False, False): raise_error,
        (False, False, True, True): raise_error,
        (False, False, True, False): raise_error,
        (False, False, False, True): raise_error,
        (False, False, False, False): raise_error
    }

    defined_by_user = (width is not None,
                       width_base_left is not None,
                       width_base_right is not None,
                       height is not None)

    try:
        width, width_base_left, width_base_right, height = (behavior[defined_by_user])()
    except KeyError:
        raise AssertionError("Behavior is not defined for the given combination of inputs.")

    widths = [0, width_base_left, width_base_right]
    y = [0, height, 0]

    t = location - width_base_left + numpy.cumsum(widths)

    return numpy.interp(t_predict, t, y)
