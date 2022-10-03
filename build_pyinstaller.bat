cd /d %~dp0
python -m pip install pyinstaller
pyinstaller --onefile --clean psd_translate.spec
pause