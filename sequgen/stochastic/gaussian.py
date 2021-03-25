import numpy


def gaussian(t_predict, stddev=1, average=0, correlation_length=0):
    """ """
    n_elems = len(t_predict)
    if correlation_length == 0:
        return average + stddev * numpy.random.randn(n_elems)

    draws = numpy.random.randn(n_elems)
    correlated = numpy.full(n_elems, numpy.nan)
    for i, _ in enumerate(t_predict):
        if i == 0:
            correlated[i] = draws[i]
        else:
            corr = max(0, (t_predict[i - 1] - t_predict[i] + correlation_length) / correlation_length)
            correlated[i] = correlated[i - 1] * corr + draws[i] * (1 - corr)
    return average + stddev * correlated
