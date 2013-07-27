import sublime
import sublime_plugin
import subprocess


class OpenWithVimCommand(sublime_plugin.WindowCommand):

    def current_line(self, view):
        row, col = view.rowcol(view.sel()[0].begin())
        row += 1
        return row

    def run(self):
        setting = sublime.load_settings("OpenWithVim.sublime-settings")
        terminal = setting.get("open_with_vim_terminal")
        terminal_option = setting.get("open_with_vim_terminal_option")
        vim_path = setting.get("open_with_vim_path")

        path = None
        if self.window.active_view():
            path = self.window.active_view().file_name()
        else:
            sublime.error_message(__name__ + ": No file to open.")
            return

        line_num = self.current_line(self.window.active_view())

        command = [terminal, terminal_option, vim_path + ' +' + str(line_num) + ' ' + path]
        subprocess.Popen(command)
