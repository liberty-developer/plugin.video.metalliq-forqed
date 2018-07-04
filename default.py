#!/usr/bin/python
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    import sys, os
    reload(sys)
    sys.setdefaultencoding("utf-8")
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'resources', 'lib'))

from xbmcswift2 import xbmcplugin
from meta import plugin
from main import *

#########   Main    #########

def main():
    if '/movies' in sys.argv[0]:
        xbmcplugin.setContent(int(sys.argv[1]), 'movies')
    elif '/tv/play' in sys.argv[0]:
        xbmcplugin.setContent(int(sys.argv[1]), 'episodes')
    elif '/tvdb' in sys.argv[0] and sys.argv[0].count('/') < 6:
        xbmcplugin.setContent(int(sys.argv[1]), 'seasons')
    elif '/tvdb' in sys.argv[0] and sys.argv[0].count('/') > 5:
        xbmcplugin.setContent(int(sys.argv[1]), 'episodes')
    elif '/tv' in sys.argv[0] and not '/settings' in sys.argv[0]:
        xbmcplugin.setContent(int(sys.argv[1]), 'tvshows')
    elif '/music' in sys.argv[0]:
        xbmcplugin.setContent(int(sys.argv[1]), 'musicvideos')
    elif '/live' in sys.argv[0]:
        xbmcplugin.setContent(int(sys.argv[1]), 'LiveTV')
    elif '/list' in sys.argv[0]:
        xbmcplugin.setContent(int(sys.argv[1]), 'videos')
    plugin.run()

if __name__ == '__main__':
    main()