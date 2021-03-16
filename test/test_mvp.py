from ts_generator.deterministic.sine import sine as signal1
from ts_generator.stochastic.white import white as noise1
from ts_generator.samplers.sample_uniform_random import sample_uniform_random
import numpy
from matplotlib import pyplot as plt


def mvp():

    class ParameterSpace:
        def __init__(self, dimension_names=None, lower_bounds=None, upper_bounds=None, sampler=None):
            self.dimension_names = dimension_names
            self.lower_bounds = lower_bounds
            self.upper_bounds = upper_bounds
            if sampler is None:
                self.sampler = sample_uniform_random
            else:
                self.sampler = sampler

        def sample(self):
            return self.sampler(dimension_names=self.dimension_names,
                                lower_bounds=self.lower_bounds,
                                upper_bounds=self.upper_bounds)

    def parameterize_noise1():
        # take a sample of noise1's parameter space according to the uniform random sampling strategy
        parameter_space = ParameterSpace(dimension_names=["stddev"],
                                         lower_bounds=numpy.asarray([0.05], dtype="float"),
                                         upper_bounds=numpy.asarray([0.1], dtype="float"))
        return parameter_space.sample()

    def parameterize_signal1():
        # take a sample of signal1's parameter space according to the uniform random sampling strategy
        parameter_space = ParameterSpace(dimension_names=["average", "amplitude", "wavelength", "phase_shift"],
                                         lower_bounds=numpy.asarray([-10, 0.1, 2, 0], dtype="float"),
                                         upper_bounds=numpy.asarray([5, 0.9, 10, 10], dtype="float"))
        return parameter_space.sample()

    # where I want the model to predict values
    t_predict = numpy.linspace(2, 20, 100)

    parameters_signal1 = parameterize_signal1()
    parameters_noise1 = parameterize_noise1()

    # generate predictions of y at t_predict using the model and the parameterization
    y_predict_signal1 = signal1(t_predict, **parameters_signal1)
    y_predict_noise1 = noise1(t_predict, **parameters_noise1)
    y_predict = y_predict_signal1 + y_predict_noise1

    # plot to verify
    plt.figure()
    plt.plot(t_predict, y_predict_signal1, 'b-', t_predict, y_predict, '.r-')
    fmt_str = "average={average:.2f}, amplitude={amplitude:.2f}, " + \
              "wavelength={wavelength:.2f}, phase_shift={phase_shift:.2f}, sttdev={stddev:.2f}"
    plt.title(fmt_str.format(**parameters_signal1, **parameters_noise1))
    plt.show()
    pass


if __name__ == "__main__":
    mvp()
