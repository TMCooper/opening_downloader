# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['opening_downloader.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('icone.ico', '.'),
        ('C:/Users/pokem/AppData/Local/ms-playwright/*', 'ms-playwright'),
        ('C:/ffmpeg/bin/ffmpeg.exe', '.'),   # si tu as ffmpeg installé
    ]
    hiddenimports=[
        'yt_dlp',
        'pytubefix',
        'selenium',
        'selenium.webdriver',
        'playwright.async_api',
        'googletrans',
        'moviepy',
        'imageio_ffmpeg'
    ],
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
    name='Opening Downloader',
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
    icon=['icone.ico'],
)
