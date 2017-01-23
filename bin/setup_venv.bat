SET VENV_DIR=.env

IF NOT EXIST %VENV_DIR% python -m venv "%VENV_DIR%"

%VENV_DIR%\Scripts\activate & pip install -r requirements.txt

