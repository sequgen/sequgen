import numpy


def normal_peak(t_predict, location=0.0, stddev=1.0, height=1.0, sign=1):

    assert sign in [-1, 1], "sign should be -1 or 1"
    max_height = 1 / (stddev * numpy.sqrt(2 * numpy.pi))
    z = (t_predict - location) / stddev
    term1 = 1 / (stddev * numpy.sqrt(2 * numpy.pi))
    term2 = numpy.exp((-1 / 2) * numpy.power(z, 2))
    return sign * height * term1 * term2 / max_height
