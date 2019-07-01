#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyinotify
import os
import sys

own = sys.argv[1]
path = sys.argv[2]

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, event):
        os.system('chown -R {0}. {1}'.format(own,event.pathname))
    def process_IN_CREATE(self, event):
        os.system('chown -R {0}. {1}'.format(own,event.pathname))
    def process_IN_MOVED_TO(self,event):
        os.system('chown -R {0}. {1}'.format(own,event.pathname))
    def process_IN_ISDIR(self,event):
        os.system('chown -R {0}. {1}'.format(own,event.pathname))

wm = pyinotify.WatchManager()
wm.add_watch(path,pyinotify.IN_MODIFY | pyinotify.IN_CREATE | pyinotify.IN_MOVED_TO | pyinotify.IN_ISDIR , rec=True,auto_add=True)
eh = EventHandler()
notifier = pyinotify.Notifier(wm, eh)
notifier.loop()




