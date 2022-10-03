# psd-translate

Translate any layer names in .psd files that contain jp/cn/kr chars to english

## usage

drop multiple .psd files onto the .exe file and translate all of them at once or run the .exe file regularly to
translate all .psd files in the current directory

## requirements

```cmd
python -m pip install psd-tools
python -m pip install google_trans_new
```

## building it yourself

with pyinstaller
```cmd
python -m pip install pyinstaller
pyinstaller --onefile --clean psd_translate.spec
```
with nuitka
```cmd
python -m pip install nuitka
python -m nuitka --follow-imports src/psd_translate/psd_translate.py
```

or use:
[build_pyinstaller.bat](../master/build_pyinstaller.bat)
[build_nuitka.bat](../master/build_nuitka.bat)

## running it without building

```cmd
Python -m relative/path/to/psd-translate.py 'path/to/example.psd' 'path/to/second/example.psd'
```

or use [psd_translate.bat](../master/psd_translate.bat)

## editing

### target language

adjust [lang](../master/psd_translate.py#L11) to change target language

### source language

currently translates anything in these unicode ranges. adjust [regex](../master/psd_translate.py#L22)

```py
jp = u'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u3400-\u4dbf]+'

cn = u'[\u3400-\u4DB5\u6300-\u77FF\u7800-\u8CFF\u8D00-\u9FCC\u2e80-\u2fd5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD]+' 
# Chinese Unicode Extension characters these aren't included because I don't know how to use them, they are just here for safekeeping
#cnExt = u'[\u20000-\u215FF\u21600-\u230FF\u23100-\u245FF\u24600-\u260FF\u26100-\u275FF\u27600-\u290FF\u29100-\u2A6DF\u2A700-\u2B734\u2B740-\u2B81D]+'

kr = u'[\uac00-\ud7a3]+'

# jp + cn + kr
regex = u'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u3400-\u4dbf\u3400-\u4DB5\u6300-\u77FF\u7800-\u8CFF\u8D00-\u9FCC\u2e80-\u2fd5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD\uac00-\ud7a3]+'
```

# libraries used

[psd-tools](https://github.com/psd-tools/psd-tools)

[google_trans_new](https://github.com/lushan88a/google_trans_new)
