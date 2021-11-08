@echo off

echo Activating venv
call .venv\scripts\activate.bat

echo Installing packages
py -m pip install pyinstaller
py -m pip install pyads

echo Finished!
pause