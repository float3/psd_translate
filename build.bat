cd /d %~dp0
pyinstaller --onefile --clean psd_translate.spec
pause