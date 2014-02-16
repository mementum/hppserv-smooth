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
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

from hpproxy import HPProxyHandler

from mipmanifest import getVideoBitrates


class MipProxyHandler(HPProxyHandler):
    server_version = "MipProxy"
    sys_version = '0.01'

    def OnRequest(self, command, path, body, headers):
        if 'QualityLevels' not in path or 'video' not in path:
            return command, path, body, headers

        mipcontrol = self.server.mipcontrol

        # Find out the bitrate
        idx = path.find('QualityLevels')
        idx = path.find('(', idx) + 1
        idx2 = path.find(')', idx)
        brate = int(path[idx:idx2])

        stats = mipcontrol.stats
        stats['seenfragments'] += 1
        seenfragments = stats['seenfragments']

        # New req avg bit rate
        unavg = stats['avgbitratereq'] * (seenfragments  - 1)
        stats['avgbitratereq'] = (unavg + brate) / seenfragments

        stats['videodatareq'] += 2 * brate

        self.postMsg(action='requestedRate', bitrate=brate)
        self.logMsg('Requested Bitrate is %d' % brate)
        if mipcontrol.started:
            self.logMsg('MipProxy Active')
            if mipcontrol.bitrate is not None and mipcontrol.bitrate < brate:
                self.logMsg('Changing bitrate to %d' % mipcontrol.bitrate)
                path = '%s%d%s' % (path[0:idx], mipcontrol.bitrate, path[idx2:])

                unavg = stats['avgbitratedown'] * (seenfragments  - 1)
                stats['avgbitratedown'] = (unavg + mipcontrol.bitrate) / seenfragments
                stats['videodatadown'] += 2 * mipcontrol.bitrate

            else:
                self.logMsg('No change of bitrate')
                unavg = stats['avgbitratedown'] * (seenfragments  - 1)
                stats['avgbitratedown'] = (unavg + brate) / seenfragments
                stats['videodatadown'] += 2 * brate


        else:
            unavg = stats['avgbitratedown'] * (seenfragments  - 1)
            stats['avgbitratedown'] = (unavg + brate) / seenfragments
            stats['videodatadown'] += 2 * brate

        stats['videodatasaved'] = stats['videodatareq'] - stats['videodatadown']
        self.postMsg(action='statistics', **stats)

        return command, path, body, headers


    def OnResponseReceived(self, command, path, body, headers, hppresp):
        mipcontrol = self.server.mipcontrol

        if mipcontrol.disablecaching and 'cache-control' in hppresp.msg:
            del hppresp.msg['cache-control']

        if not 'manifest' in path.lower():
            return

        self.logMsg('Manifest seen')
        # Potential modification of the manifest
        # http://mediadl.microsoft.com/mediadl/iisnet/smoothmedia/Experience/BigBuckBunny_720p.ism/Manifest
        manifest = hppresp.fp.read(hppresp.length) # Should close the response
        videoBitratesServer, videoBitratesClient, manifest = getVideoBitrates(manifest,
                                                                              mipcontrol.removerates,
                                                                              mipcontrol.removeratesnum)
        self.postMsg(action='videoBitrates',
                     videoBitratesServer=videoBitratesServer,
                     videoBitratesClient=videoBitratesClient)

        # Rebuild the length of manifest if changed
        if mipcontrol.removerates:
            hppresp.length = len(manifest)
            hppresp.msg['content-length'] = str(hppresp.length)

        # Put the manifest back into the response file
        hppresp.fp = StringIO(manifest)



