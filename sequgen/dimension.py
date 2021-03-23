from typing import Union


# pylint: disable=too-few-public-methods
class Dimension:
    """ """
    Bound = Union[float, int]

    def __init__(self, name: str, lower_bound: Bound, upper_bound: Bound = None):
        """ """
        self.name = name
        self.lower_bound = lower_bound
        if upper_bound is None:
            self.upper_bound = lower_bound
        else:
            self.upper_bound = upper_bound
