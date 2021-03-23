#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

# To update the package version number, edit CITATION.cff
with open('CITATION.cff', 'r') as cff:
    for line in cff:
        if 'version:' in line:
            version = line.replace('version:', '').strip().strip('"')

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='sequgen',
    version=version,
    description="Create synthetic sequence data.",
    long_description=readme + '\n\n',
    author="Generalization Team",
    author_email='generalization@esciencecenter.nl',
    url='https://github.com/sequgen/sequgen',
    packages=[
        'sequgen',
    ],
    include_package_data=True,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='sequgen',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    install_requires=[
       'matplotlib >= 3.3',
       'PyYAML >= 5.4',
       'scikit-learn >= 0.24',
       'scipy >= 1.5'
    ],
    setup_requires=[
        # dependency for `python setup.py test`
        'pytest-runner',
        # dependencies for `python setup.py build_sphinx`
        'sphinx',
        'sphinx_rtd_theme',
        'recommonmark'
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pycodestyle',
    ],
    extras_require={
        'dev':  ['prospector[with_pyroma]', 'yapf', 'isort'],
    },
    data_files=[('citation/sequgen', ['CITATION.cff'])]
)
