# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['morpion.py'],
    pathex=[],
    binaries=[],
    datas=[('support/.text.txt', 'support'), ('support/.chimique.py', 'support')],
    hiddenimports=['tkinter', '_tkinter', 'tcl'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='morpion',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
