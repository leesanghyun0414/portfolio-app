@echo off
setlocal
for /f "usebackq delims=" %%A in (`wsl wslpath "%FILE_PATH%"`) do set FILE_PATH=%%A

docker exec ^
       django_dev ^
       /bin/sh -c "black %FILE_PATH% && isort --profile black %FILE_PATH% && pylint --rcfile=./.pylintc %FILE_PATH%"
