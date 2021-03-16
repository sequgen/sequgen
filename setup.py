from setuptools import setup
from ts_generator.__version__ import __version__


setup(name="ts_generator",
      version=__version__,
      packages=["ts_generator"],
      test_suite="tests",
      install_requires=[
            "matplotlib >= 3.3",
            "PyYAML >= 5.4",
            "scikit-learn >= 0.24",
            "scipy >= 1.5"
      ],
      extras_require={
            "dev": [
                  "pytest"
            ]
      }
)
