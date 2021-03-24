import numpy


def constant(t_predict, value):
    """ """
    return numpy.ones_like(t_predict) * value
