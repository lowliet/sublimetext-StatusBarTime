#
#	Made by lowliet
#

import sublime, sublime_plugin
from datetime import datetime

class StatusBarTime(sublime_plugin.EventListener):
	def on_activated(self, view):
		Timer().displayTime(view)

class Timer():
	def displayTime(self, view):
		view.set_status('time', datetime.now().strftime('%H:%M:%S'))
		if sublime.active_window().active_view().id() == view.id():
			sublime.set_timeout(lambda: self.displayTime(view), 1000)
		else:
			view.set_status('time', '')