from ts_generator.samplers.sample_uniform_random import sample_uniform_random


class ParameterSpace:
    def __init__(self, dimensions, sampler=None):
        self.dimension_names = list()
        self.lower_bounds = list()
        self.upper_bounds = list()
        if sampler is None:
            self.sampler = sample_uniform_random
        else:
            self.sampler = sampler

        for dimension in dimensions:
            self.dimension_names.append(dimension.name)
            self.lower_bounds.append(dimension.lower_bound)
            self.upper_bounds.append(dimension.upper_bound)

        self.ndims = len(self.dimension_names)

    def __repr__(self):
        dimensions_string = ", ".join(["'{0}'".format(name) for name in self.dimension_names])
        return "{0}-D parameter space with dimensions: {1}".format(self.ndims, dimensions_string)

    def format_str(self):
        names = ["{0}={1}{0}:.2f{2}".format(name, "{", "}") for name in self.dimension_names]
        return ", ".join(names)

    def sample(self):
        return self.sampler(dimension_names=self.dimension_names,
                            lower_bounds=self.lower_bounds,
                            upper_bounds=self.upper_bounds)
