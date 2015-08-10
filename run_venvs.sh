#!/bin/sh
. venv_repo/bin/activate
myscript
deactivate
. venv_sdist/bin/activate
myscript
my_console_script
deactivate
. venv_egg/bin/activate
myscript
my_console_script
deactivate
. "venv with spaces/bin/activate"
myscript
my_console_script
deactivate
