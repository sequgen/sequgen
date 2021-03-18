from ts_generator.deterministic.sine import sine as signal1
from ts_generator.deterministic.triangular_peak import triangular_peak as signal2
from ts_generator.deterministic.constant import constant as signal3
from ts_generator.deterministic.normal_peak import normal_peak as signal4
from ts_generator.stochastic.white import white as noise1
from ts_generator.parameter_space import ParameterSpace
from ts_generator.dimension import Dimension
import numpy
from matplotlib import pyplot as plt


def mvp():

    def parameterize_noise1():
        # take a sample of noise1's parameter space according to the uniform random sampling strategy
        dims = [Dimension("stddev", 0.05, 0.1)]
        return ParameterSpace(dims).sample()

    def parameterize_signal1():
        # take a sample of signal1's parameter space according to the uniform random sampling strategy
        dims = [
            Dimension("amplitude", 0, 1),
            Dimension("average", 0.1, 0.9),
            Dimension("wavelength", 3, 5),
        ]
        return ParameterSpace(dims).sample()

    def parameterize_signal2():
        # take a sample of signal2's parameter space according to the uniform random sampling strategy
        dims = [
            Dimension("height", 1, 2),
            Dimension("placement", 0, 20),
            Dimension("width_base_left", 0.01, 2.0),
            Dimension("width_base_right", 0.01, 3.0),
        ]
        return ParameterSpace(dims).sample()

    def parameterize_signal3():
        # take a sample of signal3's parameter space according to the uniform random sampling strategy
        dims = [
            Dimension("value", 100, 200)
        ]
        return ParameterSpace(dims).sample()

    def parameterize_signal4():
        # take a sample of signal4's parameter space according to the uniform random sampling strategy
        dims = [
            Dimension("location", 3, 10),
            Dimension("stddev", 0.2, 1.2),
            Dimension("height", 0.5, 2)
        ]
        return ParameterSpace(dims).sample()

    def visualize():
        plt.figure()

        # plot signal 1
        plt.subplot(3, 2, 1)
        plt.plot(t_predict, y_predict_signal1, '.b-')
        fmt_str = "average={average:.2f}, amplitude={amplitude:.2f}, " + \
                  "wavelength={wavelength:.2f}"
        plt.title(fmt_str.format(**parameters_signal1))

        # plot signal 2
        plt.subplot(3, 2, 2)
        plt.plot(t_predict, y_predict_signal2, '.b-')
        fmt_str = "height={height:.2f}, placement={placement:.2f}, " + \
                  "width_base_left={width_base_left:.2f}, width_base_right={width_base_right:.2f}"
        plt.title(fmt_str.format(**parameters_signal2))

        # plot signal 3
        plt.subplot(3, 2, 3)
        plt.plot(t_predict, y_predict_signal3, '.b-')
        fmt_str = "value={value:.2f}"
        plt.title(fmt_str.format(**parameters_signal3))

        # plot signal 4
        plt.subplot(3, 2, 4)
        plt.plot(t_predict, y_predict_signal4, '.b-')
        fmt_str = "location={location:.2f}, stddev={stddev:.2f}, height={height:.2f}, "
        plt.title(fmt_str.format(**parameters_signal4))

        # plot noise 1
        plt.subplot(3, 2, 5)
        plt.stem(t_predict, y_predict_noise1, '.b-')
        fmt_str = "stddev={stddev:.2f}"
        plt.title(fmt_str.format(**parameters_noise1))

        # plot everything stacked
        plt.subplot(3, 2, 6)
        plt.plot(t_predict, y_predict, '.b-')
        plt.title("combined")

        plt.show()
        pass

    # where I want the model to predict values
    t_predict = numpy.linspace(-2, 20, 100)

    parameters_signal1 = parameterize_signal1()
    parameters_signal2 = parameterize_signal2()
    parameters_signal3 = parameterize_signal3()
    parameters_signal4 = parameterize_signal4()
    parameters_noise1 = parameterize_noise1()

    # generate predictions of y at t_predict using the model and the parameterization
    y_predict_signal1 = signal1(t_predict, **parameters_signal1)
    y_predict_signal2 = signal2(t_predict, **parameters_signal2)
    y_predict_signal3 = signal3(t_predict, **parameters_signal3)
    y_predict_signal4 = signal4(t_predict, **parameters_signal4)
    y_predict_noise1 = noise1(t_predict, **parameters_noise1)
    y_predict = y_predict_signal1 + y_predict_signal2 + y_predict_signal3 + + y_predict_signal4 + y_predict_noise1

    # plot to verify
    visualize()


if __name__ == "__main__":
    mvp()
