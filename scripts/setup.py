"""
This is a fake script, it is not used.
Github does not count dependent python projects unless you have a setup.py
"""

__author__ = "Alex Rogozhnikov"

from pathlib import Path

from setuptools import setup

setup(
    name="einops",
    version="0.7.0",
    description="A new flavour of deep learning operations",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/arogozhnikov/einops",
    author="Alex Rogozhnikov",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="deep learning, neural networks, tensor manipulation, machine learning, scientific computations, einops",
    install_requires=[
        # no run-time or installation-time dependencies
    ],
)
