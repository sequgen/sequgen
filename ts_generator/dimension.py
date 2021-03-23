class Dimension:
    def __init__(self, name, lower_bound, upper_bound=None):
        self.name = name
        self.lower_bound = lower_bound
        if upper_bound is None:
            self.upper_bound = lower_bound
        else:
            self.upper_bound = upper_bound
