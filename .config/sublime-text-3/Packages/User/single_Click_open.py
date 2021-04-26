import sublime
import sublime_plugin
import os

class NoPreview(sublime_plugin.EventListener):
    def on_load(self, view):
        if (os.path.exists(view.file_name())):
            view.run_command('save')