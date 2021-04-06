import numpy


def boxcar(t_predict, location, width, height=1.0):
    """Generate a time series containing boxcar function.

    Args:
      t_predict (Numpy array):
        Where you want the model to generate predictions.

      location (float):
        The start (left point) of the plateau.

      height (float):
        The height of the plateau.

      width (float):
        The width of the plateau.

    Returns:
      Numpy array of shape equal to t_predict containing the signal with the boxcar plateau.
    """

    assert width > 0, "width should be greater than zero"

    plateau = (location <= t_predict) & (t_predict <= location + width)
    boxcar_data = numpy.zeros_like(t_predict)
    boxcar_data[plateau] = height

    return boxcar_data
