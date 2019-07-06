#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setuptool Distribution for pipefish
"""

# {{{ Import
# System  Imports
import codecs
import os

# External Imports
from setuptools import setup

# }}}


def read(fname):
    """
    Read the contents of relative file.
    """
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pipefish',
    version='0.1.1dev',
    author='Tim Gates',
    author_email='tim.gates@iress.com',
    maintainer='Tim Gates',
    maintainer_email='tim.gates@iress.com',
    packages=['pipefish'],
    license='GPLv3+',
    description=(
        'Process JUnit XML and Cobertura coverage XML reports into Markdown'
    ),
    long_description=read('README.md'),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=[],
    url='https://github.com/pytest-buildkite/pipefish',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)
