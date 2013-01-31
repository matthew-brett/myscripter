################################
Playing with script installation
################################

A tiny repository to play with script installation on windows in particular.

To run the stuff here, you'll need a python on your path with virtualenv and
setuptools installed.

Start with::

    python run_setups.py

Then, on Unix::

    sh run_venvs.sh

or on Windows::

    .\run_venvs.bat

You should get something like this (on Unix)::

    Python starts at /Users/me/dev_trees/myscripter/venv_repo/bin/..
    Python starts at /Users/me/dev_trees/myscripter/venv_sdist/bin/..
    Console python starts at /Users/me/dev_trees/myscripter/venv_sdist/bin/..
    Python starts at /Users/me/dev_trees/myscripter/venv_egg/bin/..
    Console python starts at /Users/me/dev_trees/myscripter/venv_egg/bin/..
