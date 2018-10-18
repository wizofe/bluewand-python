#!/usr/bin/env python3

# Copyright (C) 2018 Ioannis Valasakis <code@wizofe.uk>
# Licensed under the GNU GPL-3
# The GNU Public License can be found in `/usr/share/common-licenses/GPL-3'.

from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='bluewand',
    version='0.1',
    description='bluewand - a simple python API for KANO Wand',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Ioannis Valasakis',
    author_email='code@wizofe.uk',
    url='https://github.com/wizofe/bluewand-python',
    python_requires='>=3.0',
    packages=['magic'],
    install_requires=[
        "bluepy"
    ],
    platforms='POSIX',
    license='GNU GPL v3'
)
