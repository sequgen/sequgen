import numpy


class Options:
    """ """

    # pylint: disable=too-many-arguments
    def __init__(self, width, width_base_left, width_base_right, height, unit_integral):
        self.width = width
        self.width_base_left = width_base_left
        self.width_base_right = width_base_right
        self.height = height
        self.unit_integral = unit_integral
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        current_values = [self.width, self.width_base_left, self.width_base_right, self.height, self.unit_integral]
        self.index += 1
        if self.index >= len(current_values):
            raise StopIteration
        return current_values[self.index]

    def _derive_for_ffft(self):
        assert self.unit_integral in [True, False], "unit_integral should be True or False"
        if self.unit_integral is True:
            # calculate width from area
            unit_area = 1.0
            self.width = (2 * unit_area) / self.height
            self._derive_for_tfft()
        else:
            raise AssertionError("Underspecified curve")
        return self

    def _derive_for_fftt(self):
        assert self.unit_integral in [True, False], "unit_integral should be True or False"
        if self.unit_integral is True:
            # calculate width from area
            unit_area = 1.0
            self.width = (2 * unit_area) / self.height
            self.width_base_left = self.width - self.width_base_right
        else:
            raise AssertionError("Underspecified curve")
        return self

    def _derive_for_ftft(self):
        assert self.unit_integral in [True, False], "unit_integral should be True or False"
        if self.unit_integral is True:
            # calculate width from area
            unit_area = 1.0
            self.width = (2 * unit_area) / self.height
            self.width_base_right = self.width - self.width_base_left
        else:
            raise AssertionError("Underspecified curve")
        return self

    def _derive_for_fttf(self):
        self._derive_for_fttt()
        self._derive_for_tttf()
        return self

    def _derive_for_fttt(self):
        self.width = self.width_base_left + self.width_base_right
        return self

    def _derive_for_tfff(self):
        self._derive_for_tfft()
        self._derive_for_tttf()
        return self

    def _derive_for_tfft(self):
        self.width_base_left = self.width / 2
        self.width_base_right = self.width / 2
        return self

    def _derive_for_tftf(self):
        self._derive_for_tftt()
        self._derive_for_tttf()
        return self

    def _derive_for_tftt(self):
        self.width_base_left = self.width - self.width_base_right
        return self

    def _derive_for_ttff(self):
        self._derive_for_ttft()
        self._derive_for_tttf()
        return self

    def _derive_for_ttft(self):
        self.width_base_right = self.width - self.width_base_left
        return self

    def _derive_for_tttf(self):
        assert self.unit_integral in [True, False], "unit_integral should be True or False"
        if self.unit_integral is True:
            # calculate height from area
            unit_area = 1.0
            self.height = (2 * unit_area) / self.width
        else:
            raise AssertionError("Underspecified curve")
        return self

    def _verify_consistency(self):
        assert self.width_base_right + self.width_base_left == self.width
        if self.unit_integral is True:
            area = 0.5 * self.width_base_left * self.height + 0.5 * self.width_base_right * self.height
            unit_area = 1.0
            assert numpy.abs(area - unit_area) < 0.00001, "curve integral does not equal unity"

    @staticmethod
    def _raise_error():
        raise AssertionError("Behavior is not defined for the given combination of inputs.")

    @staticmethod
    def _dummy():
        """ doesn't do anything"""

    def derive_undefined_values(self):
        """ """

        # The elements of the keys in the dictionary below are listed in the following order:
        # width, width_base_left, width_base_right, height. Each element denotes whether
        # the user has set them (True) or not (False).
        behavior = {
            (True, True, True, True): Options._dummy,
            (True, True, True, False): self._derive_for_tttf,
            (True, True, False, True): self._derive_for_ttft,
            (True, True, False, False): self._derive_for_ttff,
            (True, False, True, True): self._derive_for_tftt,
            (True, False, True, False): self._derive_for_tftf,
            (True, False, False, True): self._derive_for_tfft,
            (True, False, False, False): self._derive_for_tfff,
            (False, True, True, True): self._derive_for_fttt,
            (False, True, True, False): self._derive_for_fttf,
            (False, True, False, True): self._derive_for_ftft,
            (False, True, False, False): Options._raise_error,
            (False, False, True, True): self._derive_for_fftt,
            (False, False, True, False): Options._raise_error,
            (False, False, False, True): self._derive_for_ffft,
            (False, False, False, False): Options._raise_error
        }

        defined_by_user = (self.width is not None,
                           self.width_base_left is not None,
                           self.width_base_right is not None,
                           self.height is not None)

        try:
            # use the behavior dict above to choose which method to run, depending on what arguments were
            # defined by the user
            (behavior[defined_by_user])()
        except KeyError:
            raise AssertionError("Behavior is not defined for the given combination of inputs.")

        self._verify_consistency()
        return self


# pylint: disable=too-many-arguments,too-many-locals
def triangular_peak(t_predict, location, width=None, width_base_left=None, width_base_right=None, height=None,
                    unit_integral=False):
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

      unit_integral (bool):
        When true, the integral of the curve sums to unity.

    Returns:
      Numpy array of shape equal to t_predict containing the curve for a triangular peak in user-defined units.
    """

    if width_base_left is not None:
        assert width_base_left > 0, "width_base_left should be > 0"
    if width_base_right is not None:
        assert width_base_right > 0, "width_base_right should be > 0"
    if width is not None:
        assert width > 0, "width should be > 0"

    # Use the Options object to derive values for any arguments left unspecified
    args = width, width_base_left, width_base_right, height, unit_integral
    width, width_base_left, width_base_right, height, unit_integral = \
        Options(*args).derive_undefined_values()

    widths = [0, width_base_left, width_base_right]
    y = [0, height, 0]

    t = location - width_base_left + numpy.cumsum(widths)

    return numpy.interp(t_predict, t, y)
