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
import xml.etree.ElementTree as ElementTree


def getVideoBitrates(manifest, removerates=False, removeratesnum=0):

    videoBitratesServer = list()
    elemroot = ElementTree.fromstring(manifest)

    for streamIndex in list(elemroot):
        if streamIndex.get('Type') != 'video':
            continue

        for qualityLevel in streamIndex.findall('QualityLevel'):
            videoBitratesServer.append(int(qualityLevel.get('Bitrate')))

        videoBitratesServer.sort()
        videoBitratesClient = videoBitratesServer[:]

        if removerates and videoBitratesServer:
            while removeratesnum and videoBitratesClient:
                del videoBitratesClient[-1]
                removeratesnum -= 1

            if not videoBitratesClient:
                videoBitratesClient.append(videoBitratesServer[0])

            toRemove = list()
            for qualityLevel in streamIndex.findall('QualityLevel'):
                bitrate = int(qualityLevel.get('Bitrate'))
                if bitrate not in videoBitratesClient:
                    toRemove.append(qualityLevel)

            for elem in toRemove:
                streamIndex.remove(elem)

    if removerates:
        manifest = ElementTree.tostring(elemroot, encoding='UTF-8')

    return videoBitratesServer, videoBitratesClient, manifest
