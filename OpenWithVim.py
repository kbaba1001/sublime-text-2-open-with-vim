import sublime
import sublime_plugin
import subprocess

class OpenWithVimCommand(sublime_plugin.WindowCommand):
    def run(self):
        setting = sublime.load_settings("OpenWithVim.sublime-settings")
        terminal = setting.get("open_with_vim_terminal")
        terminal_option = setting.get("open_with_vim_terminal_option")
        vim_path = setting.get("open_with_vim_path")

        path = None
        if self.window.active_view():
            path = "\"" + self.window.active_view().file_name() + "\""
        else:
            sublime.error_message(__name__ + ": No file to open.")
            return

        args = [terminal, option, vim + " " + path]
        subprocess.Popen(args)
