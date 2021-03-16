import numpy


def normal_peak(t_predict, location=0.0, stddev=1.0, height=1.0):

    max_height = 1 / (stddev * numpy.sqrt(2 * numpy.pi))
    z = (t_predict - location) / stddev
    term1 = 1 / (stddev * numpy.sqrt(2 * numpy.pi))
    term2 = numpy.exp((-1 / 2) * numpy.power(z, 2))
    return height * term1 * term2 / max_height
