import numpy


# pylint: disable=too-many-arguments
def triangular_peak(t_predict, width_leading=None, width_base_left=None, width_base_right=None, width_trailing=None,
                    width=1.0, height=1.0, placement=0, sign=1):
    """ """

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

    t = placement + numpy.cumsum(widths)

    return sign * numpy.interp(t_predict, t, y)
