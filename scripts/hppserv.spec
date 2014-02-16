#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# 
# This file is part of MipProxy
#
# MipProxy is a Microsoft Smooth Streaming Proxy Controller
# Copyright (C) 2011 Daniel Rodriguez
#
################################################################################

import compileall
compileall.compile_dir('./mipdemo', force=True)

a = Analysis([os.path.join(HOMEPATH,'support/_mountzlib.py'),
              os.path.join(HOMEPATH,'support/useUnicode.py'),
              'mipdemo/mipdemo.pyw'],	
             pathex=None)

pyz = PYZ(a.pure)

exe = EXE(pyz,
          a.scripts + [('OO', '', 'OPTION')],
          console=False,
          debug=False,
          name=os.path.join('build/pyi.win32/mipdemo', 'mipdemo.exe'),
          exclude_binaries=1,
          strip=False,
          upx=False,
          )

coll = COLLECT(exe,
               a.binaries,
               [],
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name=os.path.join('dist', 'mipdemo'))
