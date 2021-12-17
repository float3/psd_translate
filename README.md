# psd-translate

Translate any layer names in .psd files that contain jp/cn/kr chars to english

# usage 

drop multiple .psd files onto the .exe file and translate all of them at once
or start the .exe file regularly to translate all .psd files in the current directory

# building it yourself

Requirements

python

in cmd

```cmd
pip install pyinstaller
```

```cmd
pyinstaller --onefile --clean 'path/to/psd-translate.spec'
```

# running it without building

```cmd
Python 'relative/path/to/psd-translate.py' 'path/to/example.psd 'path/to/second/example.psd'
```

# editing

currently translates anything in these unicode ranges

```py
jp = u'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]+'

cn = u'[\u3400-\u4DB5\u4E00-\u62FF\u6300-\u77FF\u7800-\u8CFF\u8D00-\u9FCC\u2e80-\u2fd5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD\u20000-\u215FF\u21600-\u230FF\u23100-\u245FF\u24600-\u260FF\u26100-\u275FF\u27600-\u290FF\u29100-\u2A6DF\u2A700-\u2B734\u2B740-\u2B81D]+'

kr = u'[\uac00-\ud7a3]+'

# jp + cn + kr
regex = u'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u3400-\u4dbf\u3400-\u4DB5\u6300-\u77FF\u7800-\u8CFF\u8D00-\u9FCC\u2e80-\u2fd5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD\uac00-\ud7a3]+'```

edit [L17](../blob/master/psd-translate.py#17) to change target language

# libraries used

[psd-tools](https://github.com/psd-tools/psd-tools)

[google_trans_new](https://github.com/lushan88a/google_trans_new)