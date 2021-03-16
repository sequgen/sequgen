import numpy


def white(t_predict, stddev=1, average=0):
    n_elems = len(t_predict)
    return average + stddev * numpy.random.randn(n_elems)
