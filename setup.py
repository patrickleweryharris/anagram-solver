# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('anagram_solver/anagram_solver.py').read(), re.M).group(1)

setup(
    name="anagram_solver",
    packages=["anagram_solver"],
    entry_points={"console_scripts": ['anagram_solver = anagram_solver.anagram_solver:main']},
    version=version,
    description="Python command line application bare bones template.",
    long_description="Solve anagrams using a dictionary of close to one hundred thousand English words",
    author="Patrick Lewery Harris",
    author_email="patrick@plh.io",
    url="https://github.com/patrickleweryharris/anagram-solver",)
