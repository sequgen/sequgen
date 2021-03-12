# Time Series Generator
Create synthetic time series data of defined type (or class).

## Time series classes
A times series class can be provided as a Python dictionary or loaded from yaml files.
The class description needs to contain all necessary characteristics of both signal (``signal_defs``) and noise (``noise_defs``).

## Install

```shell
# make a virtual environment
python -m venv venv3

# activate the virtual environment
source venv3/bin/activate

# upgrade pip 
pip install --upgrade pip

# install the package
pip install .

# install the package's development dependencies
pip install .[dev]

# test if the unit tests work
pytest
```

### Example of a time series class definition




```python
TSC_01 = {'class_name': 'Simple example',
          'n_timepoints': 400,
          'n_channels': 6,
          'signal_defs': [{'peaks_per_ch' : 1,
                           'channels' : [3,4,5],
                           'n_ch' : [2, 3],
                           'length' : [50,80],
                           'position' : [50,160],
                           'extra_shift' : [-10,10],
                           'amp' : [0.7,1],
                           'sign' : 1,
                           'signal_type' : 'peak_exponential'
                         }],
          'noise_defs': [{'channels' : 'all',
                           'noise_amp' : [0.05,0.06],
                          'noise_type' : 'gaussian'
                         },
                         {'channels' : 'all',
                          'noise_amp' : [0.018,0.022],
                          'noise_type' : 'random_walk'
                         }]
          }
```
The defined class can then be used to generate according time series. 
```python
import TS_generator as TSgen
import TS_plotting as TSplot

X = TSgen.generate_TS(TSC_01,
                       random_seed = None,
                       ignore_noise = False)

TSplot.plot_TS(X, TSC_01)
```
![](documentation/time_series_example.png?raw=true)
