@echo off
@REM venv\Scripts\activate.bat

@REM start /B /wait cmd /c set FLASK_ENV=development & flask run
set FLASK_ENV=development
flask run

