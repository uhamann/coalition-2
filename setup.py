# -*- coding: utf-8 -*-

import sys

from setuptools import setup, find_packages
from setuptools.extension import Extension

try:
    from Cython.Build import cythonize
except ImportError:
    raise RuntimeError(
        "Cython required for running the package installation\n"
        + "Try installing it with:\n"
        + "$> pip install cython"
    )

try:
    import numpy
except ImportError:
    raise RuntimeError(
        "Numpy required for running the package installation\n"
        + "Try installing it with:\n"
        + "$> pip install numpy"
    )

# Define common arguments used to compile the extensions
common_link_args = ["-fopenmp"]
common_compile_args = ["-fopenmp", "-O3", "-ffast-math"]
common_include = [numpy.get_include()]

#if sys.platform.startswith("darwin"):
#    common_link_args.append("-Wl,-rpath,/usr/local/opt/gcc/lib/gcc/9/")


#external_modules = cythonize(extensions, force=True, language_level=3)

requirements = [
    "wheel",
    "setuptools>=40.8.0",
    "numpy",
]

setup(
    name="coalition-2",
    version="0.5",
    author="Ulrich Hamann, Elena Leonarduzzi",
    packages=find_packages(),
    license="LICENSE",
    include_package_data=True,
    description="Python framework for detecting thunderstorms with MSG satellite observations",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    url="https://coalition-2.github.io/",
    project_urls={
        "Source": "https://github.com/coalition-2/coalition-2",
        "Issues": "https://github.com/coalition-2/coalition-2/issues",
        "CI": "https://github.com/coalition-2/coalition-2/actions",
        "Changelog": "https://github.com/coalition-2/coalition-2/releases",
        "Documentation": "https://coalition-2.readthedocs.io",
    },
    setup_requires=requirements,
    install_requires=requirements,
)
