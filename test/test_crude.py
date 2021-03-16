from ts_generator.TS_generator import generate_TS as generate_time_series
import numpy


def test_crude():

    constraints = {
        'class_name': 'Simple example',
        'n_timepoints': 400,
        'n_channels': 6,
        'signal_defs': [
            {
                'peaks_per_ch': 1,
                'channels': [3, 4, 5],
                'n_ch': [2, 3],
                'length': [50, 80],
                'position': [50, 160],
                'extra_shift': [-10, 10],
                'amp': [0.7, 1],
                'sign': 1,
                'signal_type': 'peak_exponential'
             }
         ],
        'noise_defs': [
            {
                'channels': 'all',
                'noise_amp': [0.05, 0.06],
                'noise_type': 'gaussian'
            }, {
                'channels': 'all',
                'noise_amp': [0.018, 0.022],
                'noise_type': 'random_walk'
            }
        ]
    }

    simulated = generate_time_series(constraints, random_seed=None, ignore_noise=False)

    assert simulated is not None
    assert isinstance(simulated, numpy.ndarray)
    assert simulated.shape == (6, 400)
