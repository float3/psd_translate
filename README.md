# psd-translate

Translate layer names in .psd files from jp/cn/kr or specifically anything in this unicode range [\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]

edit [L22](../blob/master/translate.py#22) to change target language

edit dropPSDhere.bat and change "yourPythonPathHere" to your python install-path to drop multiple .psd files onto the .bat file and translate all of them at once
otherwise use 

```cmd
Python [relative/path/to/translate.py] [input_file_path1] [input_file_path2] ...
```

if a [input_file_path] doesn't end in .psd it will be ignored.
you can specify multiple

