# (c) Copyright 2024 cjones

""" Simple setup to define the entry point for the main module"""

import setuptools

setuptools.setup(
    name='elgato_state',
    version='1.0.0',
    install_requires=[],
    packages=setuptools.find_packages(),
    entry_points='''
        [console_scripts]
        elgato_state=elgato_state.shell:cli
    ''',
)
