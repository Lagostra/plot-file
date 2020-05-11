from setuptools import setup, find_packages

version_string = '0.0.9'

description = 'A script for quickly plotting data from a text file.'

setup(
    name='plot_file',
    version=version_string,
    packages=find_packages(),

    install_requires=[
        "pandas>=1.0.3",
        "matplotlib>=3.2.1",
        "numpy>=1.18.4",
        "seaborn>=0.10.1"
    ],

    author='Eivind Lie Andreassen',
    description=description,
    long_description=description,

    entry_points={
        "console_scripts": [
            "plot_file = plot_file:main"
        ]
    }
    
)