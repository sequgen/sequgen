# Coverage reporting

The coverage reports will be written in this directory. After running `pytest`, the directory should look more or less like this:

```text
.
├── coverage.xml
├── htmlcov
│   ├── coverage_html.js
│   ├── favicon_32.png
│   ├── index.html
│   ├── jquery.ba-throttle-debounce.min.js
│   ├── jquery.hotkeys.js
│   ├── jquery.isonscreen.js
│   ├── jquery.min.js
│   ├── jquery.tablesorter.min.js
│   ├── keybd_closed.png
│   ├── keybd_open.png
│   ├── sequgen_deterministic_constant_py.html
│   ├── sequgen_deterministic___init___py.html
│   ├── sequgen_deterministic_normal_peak_py.html
│   ├── sequgen_deterministic_sine_py.html
│   ├── sequgen_deterministic_triangular_peak_py.html
│   ├── sequgen_dimension_py.html
│   ├── sequgen___init___py.html
│   ├── sequgen_parameter_space_py.html
│   ├── sequgen_samplers___init___py.html
│   ├── sequgen_samplers_sample_uniform_random_py.html
│   ├── sequgen_stochastic_gaussian_py.html
│   ├── sequgen_stochastic___init___py.html
│   ├── status.json
│   └── style.css
└── README.md
```

Everything except the README is generated (see configuration in `/.coveragerc`).

