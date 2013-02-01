from os.path import join as pjoin
from distutils.core import setup

setup(
    name='myscripter',
    version='1.0',
    scripts=[pjoin('bin', 'myscript')]
    )
