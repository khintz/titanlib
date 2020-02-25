#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from distutils.command.build import build as build_orig
from distutils.core import setup, Extension
from setuptools import setup, Extension
import glob
import itertools

__version__ = '${PROJECT_VERSION}'

def partition(pred, iterable):
    t1, t2 = itertools.tee(iterable)
    return itertools.filterfalse(pred, t1), filter(pred, t2)


class build(build_orig):
    def finalize_options(self):
        super().finalize_options()
        condition = lambda el: el[0] == 'build_ext'
        rest, sub_build_ext = partition(condition, self.sub_commands)
        self.sub_commands[:] = list(sub_build_ext) + list(rest)

sources = '${SOURCES}'.split(';') + ['${CMAKE_CURRENT_SOURCE_DIR}/SWIG/titanlib.i'],
print("SOURCES:", sources)

example_module = Extension('_titanlib',
        #sources='${SOURCES}'.split(';') + ['${CMAKE_CURRENT_SOURCE_DIR}/../titanlib.i'],
        sources='${SOURCES}'.split(';') + ['${SWIG_INTERFACE}'],
        language="c++",
        swig_opts=['-I../../../include', '-c++', '-I/usr/include/python3.6m'],
        libraries=["gsl", "gslcblas", "proj"],
        library_dirs=["/usr/lib/x86_64-linux-gnu/"],
        include_dirs=['../../../include']
        )

setup (
    name='titanlib',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=__version__,

    description='A quality control toolbox',

    # The project's main homepage.
    url='https://github.com/metno/titanlib',

    # Author details
    author='Cristian Lussana',
    author_email='cristianl@met.no',

    # Choose your license
    license='LGPL-3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'Topic :: Scientific/Engineering :: Information Analysis',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    # What does your project relate to?
    keywords='meteorology quality control observation weather',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', '*tests*']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['numpy>=1.7', 'scipy', 'six', 'future'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
    #    'dev': ['check-manifest'],
        'test': ['coverage', 'pep8'],
    #    'test': ['pytest'],
    },

    test_suite="titanlib.tests",
    ext_modules = [example_module],
    cmdclass={'build': build},
)
