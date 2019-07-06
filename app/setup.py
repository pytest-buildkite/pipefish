"""
Setuptool Distribution for pipefish
"""
from setuptools import setup

setup(
    name='pipefish',
    version='0.1.1dev',
    author='Tim Gates',
    author_email='tim.gates@iress.com',
    packages=['pipefish'],
    license='GPLv3+',
    long_description=(
        'Process JUnit XML and Cobertura coverage XML reports into Markdown'
    ),
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
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
