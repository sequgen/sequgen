import numpy


def constant(t_predict, value):
    """Generates a time series array with constant value.

    Generates a time series array with constant value `value` for all elements in `t_predict`.

    Args
      t_predict:
        Numpy array containing the points in time where you want to generate a prediction using the 'constant' model.
      value:
        Value of the dependent variable. Constant for all values of `t` in `t_predict`

    Returns:
      Numpy array with equal shape as that of `t_predict`, filled with constant value `value`
    """
    return numpy.ones_like(t_predict) * value
