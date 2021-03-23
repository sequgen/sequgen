from sequgen.deterministic.triangular_peak import triangular_peak
from sequgen.parameter_space import ParameterSpace
from sequgen.dimension import Dimension
import numpy
from matplotlib import pyplot as plt


def test_mvp():

    # where I want the model to predict values
    t_predict = numpy.linspace(-2, 20, 100)

    parameter_space = ParameterSpace([
        Dimension("height", 1, 2),
        Dimension("placement", 3, 10),
        Dimension("width_base_left", 0.5),
        Dimension("width_base_right", 2.0, 3.0),
    ])

    # draw a sample of the parameter space for each space
    parameters = parameter_space.sample()

    # generate predictions of y at t_predict using the model and the parameterization
    y_predict = triangular_peak(t_predict, **parameters)

    # plot to verify
    plt.figure()
    plt.plot(t_predict, y_predict, '.b-')
    plt.title(parameter_space.format_str().format(**parameters))
    plt.show()


if __name__ == "__main__":
    test_mvp()
