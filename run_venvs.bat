call venv_repo\Scripts\activate.bat
call myscript
call deactivate
call venv_sdist\Scripts\activate.bat
call myscript
call my_console_script
call deactivate
call venv_egg\Scripts\activate.bat
call myscript
call my_console_script
call deactivate
call venv_exe\Scripts\activate.bat
call myscript
call deactivate
call "venv with spaces\Scripts\activate.bat"
call myscript
call deactivate
