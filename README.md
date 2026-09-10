# psd_translate

Translates Japanese, Chinese and Korean layer names in `.psd` files to English.

## Install

```sh
pip install -r requirements.txt
```

## Usage

```sh
python src/psd_translate/psd_translate.py a.psd b.psd
```

Without arguments it translates every `.psd` in the current directory, so a built exe can be dropped into a folder or have files dropped onto it. `psd_translate.bat` wraps the same call.

Change the target language and the detected script ranges at the top of `psd_translate.py`.

## Build an exe

`build_pyinstaller.bat` or `build_nuitka.bat`.
