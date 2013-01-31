from os.path import join as pjoin
from distutils.core import setup

setup(
    name='myscripter',
    version='1.0',
    packages=['myscripter'],
    scripts=[pjoin('bin', 'myscript')],
    # This next one is specific to setuptools installs
    entry_points={
        'console_scripts': [
            'my_console_script = myscripter.commands:my_console_script',
        ]
    }
    )
