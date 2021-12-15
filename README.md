# psd-translate

Translate layer names in .psd files from jp/cn/kr or specifically anything in this unicode range [\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]

edit [L15](../blob/master/psd-translate.py#15) to change target language

drop multiple .psd files onto the .bat file and translate all of them at once

or start the .bat file regularly to translate all .psd files in the current directory

```cmd
Python [relative/path/to/psd-translate.py] [input_file_path1] [input_file_path2] ...
```

if a [input_file_path] doesn't end in .psd it will be ignored.
you can specify multiple