# `sequgen`

## Purpose

Programmatically generate synthetic sequence data such as time series, strings, DNA, etc. 
Sequence data generation is fully controlled by the user. 
sequgen does not build models from real-world sequence data.

## Badges

| fair-software.nl recommendations | |
| :-- | :--  |
| (1/5) code repository              | [![github repo badge](https://img.shields.io/badge/github-repo-000.svg?logo=github&labelColor=gray&color=blue)](https://github.com/sequgen/sequgen) |
| (2/5) license                      | [![github license badge](https://img.shields.io/github/license/sequgen/sequgen)](https://github.com/sequgen/sequgen) |
| (3/5) community registry           | [![pypi badge](https://img.shields.io/pypi/v/sequgen.svg?colorB=blue)](https://pypi.python.org/pypi/sequgen/) |
| (4/5) citation                     | [![zenodo badge](https://zenodo.org/badge/DOI/10.0000/FIXME.svg)](https://doi.org/10.0000/FIXME) |
| (5/5) checklist                    | [![core infrastructures badge](https://bestpractices.coreinfrastructure.org/projects/4630/badge)](https://bestpractices.coreinfrastructure.org/en/projects/4630) |
| overall                            | [![fair-software badge](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F-green)](https://fair-software.eu) |
| **Other best practices**
| Documentation                      | [![Documentation Status](https://readthedocs.org/projects/sequgen/badge/?version=latest)](https://sequgen.readthedocs.io/en/latest/?badge=latest) |
| Supported Python versions          | [![python versions badge](https://img.shields.io/pypi/pyversions/sequgen.svg)](https://pypi.python.org/pypi/sequgen) |
| Code quality                       | [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=sequgen_sequgen&metric=alert_status)](https://sonarcloud.io/dashboard?id=sequgen_sequgen) |
| Code coverage of unit tests        | [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=sequgen_sequgen&metric=coverage)](https://sonarcloud.io/dashboard?id=sequgen_sequgen) |
| **GitHub Actions**
| Citation metadata consistency      | [![workflow cffconvert badge](https://github.com/sequgen/sequgen/workflows/cffconvert/badge.svg)](https://github.com/sequgen/sequgen/actions?query=workflow%3A%22cffconvert%22) |
| Unit tests                         | [![workflow tests badge](https://github.com/sequgen/sequgen/workflows/tests/badge.svg)](https://github.com/sequgen/sequgen/actions?query=workflow%3Atests) |

## Install

``` {.sourceCode .console}
pip3 install sequgen
```


## Usage example

This usage example involves generating time series data. We generate a time series with
three channels: 1. a normal distribution, 2. Gaussian noise, and 3. the combination (sum) 
of the first two channels. The normal distribution is positioned between 8 and 12 on an
abstract time axis of 100 intervals starting at 0 and ending at 20. The standard deviation
of the distribution is a value between 1 and 2 and its peak has a height between 4 and 5.
For the Gaussian noise we use the default values (standard deviation 1 and average value 0).
The third channel is defined as the sum of the other two channels. After creating the
three channels, graphs with their values are plotted:

```python
from matplotlib import pyplot as plt
import numpy
from sequgen.deterministic.normal_peak import normal_peak
from sequgen.stochastic.gaussian import gaussian
from sequgen.parameter_space import ParameterSpace
from sequgen.dimension import Dimension

time_axis = numpy.linspace(start=0, stop=20, num=101)
parameter_space_0 = ParameterSpace([
    Dimension("location", 8, 12),
    Dimension("stddev", 1, 2),
    Dimension("height", 4, 5),
])

channels = []
channels.append(normal_peak(time_axis, **parameter_space_0.sample()))
channels.append(gaussian(time_axis))
channels.append(channels[0] + channels[1])
titles = [ "channel 1: normal peak", "channel 2: gaussian noise", "channel 3: combined" ]

for i in range(0, len(channels)):
    plt.subplot(len(channels), 1, i+1)
    plt.plot(time_axis, channels[i])
    plt.title(titles[i], y=0.75, x=0.01, loc="left")
plt.show()
```

And these are the results:

![alt text](images/usage_example.png)

## Contributing

For developer documentation, go to the [developer's README](README.dev.md).

If you want to contribute to the development of `sequgen`, have a look
at the [contribution guidelines](CONTRIBUTING.rst).

## Credits

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[NLeSC/python-template](https://github.com/NLeSC/python-template).
