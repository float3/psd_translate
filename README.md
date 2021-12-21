# psd-translate

Translate any layer names in .psd files that contain jp/cn/kr chars to english

## usage

drop multiple .psd files onto the .exe file and translate all of them at once or run the .exe file regularly to
translate all .psd files in the current directory

### building it yourself

requirements

```cmd
pip install pyinstaller
```

building

```cmd
pyinstaller --onefile --clean psd-translate.spec
```

or use [build.bat](../blob/master/build.bat)

### running it without building

```cmd
Python -m relative/path/to/psd-translate.py 'path/to/example.psd 'path/to/second/example.psd'
```

or use [psd-translate.bat](../blob/master/psd-translate.bat)

## editing

### target language

adjust [lang](../blob/master/psd-translate.py#L10) to change target language

### source language

currently translates anything in these unicode ranges. adjust [regex](../blob/master/psd-translate.py#L21)

```py
jp = u'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u3400-\u4dbf]+'

cn = u'[\u3400-\u4DB5\u6300-\u77FF\u7800-\u8CFF\u8D00-\u9FCC\u2e80-\u2fd5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD]+' 
# Chinese Unicode Extension characters these aren't included because I don't know how to use them, they are just here for safekeeping
#cnExt = u'[\u20000-\u215FF\u21600-\u230FF\u23100-\u245FF\u24600-\u260FF\u26100-\u275FF\u27600-\u290FF\u29100-\u2A6DF\u2A700-\u2B734\u2B740-\u2B81D]+'

kr = u'[\uac00-\ud7a3]+'

# jp + cn + kr
regex = u'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u3400-\u4dbf\u3400-\u4DB5\u6300-\u77FF\u7800-\u8CFF\u8D00-\u9FCC\u2e80-\u2fd5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD\uac00-\ud7a3]+'
```

I haven't tested just letting google translate handle the translation automatically but
replacing [L48-51](../blob/master/psd-translate.py#L48-L51) with

```py
	layer.name = translator.translate(layer.name, lang)
	filetouched = True
	printindent('translated layer: ' + layer.name)
```

might also work

# libraries used

[psd-tools](https://github.com/psd-tools/psd-tools)

[google_trans_new](https://github.com/lushan88a/google_trans_new)