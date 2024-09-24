@echo off
color 5
title Installing Dependencies...

python --version
if %errorlevel%==0 (
    echo Python Is Installed
) else (					
echo		Du musch no Python abelade
)

cd /d "%~dp0"
python.exe -m pip install --upgrade pip

echo Installing Requirements...
python -m pip install -r requirements.json

pause