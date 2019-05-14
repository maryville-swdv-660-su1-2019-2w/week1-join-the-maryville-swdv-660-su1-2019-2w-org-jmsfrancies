# -*- mode: python -*-

block_cipher = None


a = Analysis(['SWDV660.py'],
             pathex=['C:\\Users\\HPelite800G1\\Documents\\GitHub\\week1-join-the-maryville-swdv-660-su1-2019-2w-org-jmsfrancies\\SWDV-660-Week1'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
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
          name='TheMenu',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
