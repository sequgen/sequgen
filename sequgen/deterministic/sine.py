import numpy


def sine(t_predict, wavelength, phase_shift=0, amplitude=1.0, average=0.0):
    """Generates a sine curve.

    Args:
      t_predict:
        Numpy array with points in time where you want the model to generate predictions.
      phase_shift:
        How much the phase is shifted in units of t_predict
      amplitude:
        Amplitude of the sine.
      wavelength:
        Wavelength of the sine in units of t_predict.
      average:
        What the average of the sine wave is, i.e. how much the sine wave is offset from y=0.

    Returns:
      Numpy array with shape equal to t_predict, containing the y values for the sine wave curve.
    """

    return average + amplitude * numpy.sin(2 * numpy.pi * (t_predict - phase_shift) / wavelength)
