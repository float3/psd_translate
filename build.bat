cd /d %~dp0
pyinstaller --onefile --clean psd-translate.spec
pause