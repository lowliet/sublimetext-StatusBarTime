#
#    Made by lowliet
#

import sublime, sublime_plugin
from datetime import datetime

class StatusBarTime(sublime_plugin.EventListener):
    def on_activated(self, view):
        settings = sublime.load_settings('StatusBarTime.sublime-settings')
        Timer(settings.get(STATUSBARTIME_FORMAT_KEY, DEFAULT_FORMAT)).displayTime(view)

class Timer():
    def __init__(self, format):
        self._format = format

    def displayTime(self, view):
        view.set_status('time', datetime.now().strftime(self._format))
        if sublime.active_window().active_view().id() == view.id():
            sublime.set_timeout(lambda: self.displayTime(view), 1000)
        else:
            view.set_status('time', '')

STATUSBARTIME_FORMAT_KEY = 'StatusBarTime_format'
DEFAULT_FORMAT = '%H:%M:%S'