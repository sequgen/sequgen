import numpy


def sine(t_predict, wavelength, phase_shift=0, amplitude=1.0, average=0.0):
    """ """
    return average + amplitude * numpy.sin(2 * numpy.pi * (t_predict - phase_shift) / wavelength)
