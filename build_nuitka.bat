cd /d %~dp0
python -m pip install nuitka
python -m nuitka --follow-imports src/psd_translate/psd_translate.py
pause