from typing import Union


# pylint: disable=too-few-public-methods
class Dimension:
    """Class representing one dimension of a parameter space."""
    Bound = Union[float, int]

    def __init__(self, name: str, lower_bound: Bound, upper_bound: Bound = None):
        """Constructor

        Constructor.

        Args:
          name (str):
            Name of the dimension.
          lower_bound (Bound):
            Lower bound of the dimension.
          upper_bound (Bound):
            Upper bound of the dimension.
        """
        self.name = name
        self.lower_bound = lower_bound
        if upper_bound is None:
            self.upper_bound = lower_bound
        else:
            self.upper_bound = upper_bound
