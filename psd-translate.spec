# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['psd-translate.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=['aggdraw', 'altgraph', 'attrs', 'autopep8', 'backports.entry-points-selectable', 'certifi', 'charset-normalizer', 'distlib', 'docopt', 'filelock', 'future', 'future-fstrings', 'google-translator', 'idna', 'imageio', 'networkx', 'numpy', 'packaging', 'pefile', 'Pillow', 'pip', 'platformdirs', 'psd-tools', 'pycodestyle', 'pyinstaller', 'pyinstaller-hooks-contrib', 'pyparsing', 'PyWavelets', 'pywin32-ctypes', 'requests', 'scikit-image', 'scipy', 'setuptools', 'six', 'tifffile', 'toml', 'urllib3', 'virtualenv', 'wheel'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='psd-translate',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
