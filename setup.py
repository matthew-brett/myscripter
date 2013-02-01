import setuptools
from distutils.core import setup

setup(
    name='myscripter',
    version='1.0',
    packages = ['myscripter'],
    entry_points = {
        'console_scripts': [
            'my_console_script = myscripter.commands:my_console_script']
    }
    )
