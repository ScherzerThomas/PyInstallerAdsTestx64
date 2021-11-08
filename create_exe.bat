@echo off

echo Activating venv
call .venv\scripts\activate.bat

echo Create executable
pyinstaller TestScript.py --onefile --debug=all

echo Finished!
pause