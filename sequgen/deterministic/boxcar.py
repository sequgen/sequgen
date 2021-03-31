import numpy


def boxcar(t_predict, location=1.0, height=1.0, width=1.0):
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

    def boxcar_value(value, location, height, width):
        if value < location or value > location + width:
            return 0
        return height

    if width < 0:
        location = location + width
        width = -width

    return numpy.array([boxcar_value(value, location, height, width) for value in t_predict])
