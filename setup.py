#!/usr/bin/env python
import os
from sequgen.__version__ import __version__

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="sequgen",
    version=__version__,
    description="Create synthetic sequence data.",
    long_description=readme + "\n\n",
    long_description_content_type="text/markdown",
    author="Generalization Team",
    author_email="generalization@esciencecenter.nl",
    url="https://github.com/sequgen/sequgen",
    packages=[
        "sequgen",
        "sequgen.deterministic",
        "sequgen.samplers",
        "sequgen.stochastic"
    ],
    include_package_data=True,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords="sequgen",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    test_suite="tests",
    install_requires=[
        "matplotlib >= 3.3",
        "PyYAML >= 5.4",
        "scikit-learn >= 0.24",
        "scipy >= 1.5"
    ],
    setup_requires=[
    ],
    tests_require=[
    ],
    extras_require={
        "dev":  [
            "isort",
            "prospector[with_pyroma]",
            "pycodestyle",
            "pytest-cov",
            "pytest-runner",
            "pytest",
            "recommonmark",
            "sphinx_rtd_theme",
            "sphinx",
            "yapf"
        ],
    },
    data_files=[("citation/sequgen", ["CITATION.cff"])]
)
