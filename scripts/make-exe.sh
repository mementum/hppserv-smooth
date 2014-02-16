#! /bin/sh
################################################################################
# 
# This file is part of MipProxy
#
# MipProxy is a Microsoft Smooth Streaming Proxy Controller
# Copyright (C) 2011 Daniel Rodriguez
#
################################################################################
# to create spec
# python ../pyinstaller/Makespec.py -s -w bfplusplus.pyw -o exe

find . -name '*~' -exec rm -f {} \;
find . -name '*.pyc' -exec rm -f {} \;
find . -name '*.pyo' -exec rm -f {} \;

rm -rf bin

mkdir -p bin/pkg
cp scripts/hppserv.spec bin/pkg

python -OO ../pyinstaller/Build.py -y bin/pkg/hppserv.spec
mv logdict* bin/pkg

