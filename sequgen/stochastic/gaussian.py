import numpy


def gaussian(t_predict, stddev=1.0, average=0.0, correlation_length=0.0):
    """Generate an array with an optionally autocorrelated time series of draws from a Normal distribution.

    Args:
      t_predict (Numpy array):
        points in time where you want to generate a prediction using this model.
      stddev (float):
        standard deviation of the Normal distribution that we will be drawing random samples from.
      average (float):
        mean of the Normal distribution that we will be drawing samples from.
      correlation_length (float):
        Correlation length in units of `t_predict`. Default is 0.0, for uncorrelated samples.

    Returns:
      Numpy array of shape equal to t_predict, where each elem is a random and optionally autocorrelated draw from
      a Normal distribution.
    """
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
