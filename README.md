# psd-translate

Translate layer names in .psd files from japanese to english

edit dropPSDhere.bat and change "yourPythonPathHere" to your python install-path to drop multiple .psd files onto the .bat file and translate all of them at once
otherwise use 

```cmd
Python -m python [relative/path/to/translate.py] [input_file_path1] [input_file_path2] ...
```

if a [input_file_path] doesn't end in .psd it will be ignored.
you can specify multiple
