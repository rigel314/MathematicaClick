import sublime, sublime_plugin, time

class MathematicaClickSelectCommand(sublime_plugin.TextCommand) :
	def run(self, edit) :
		reg = self.view.sel()[0]
		i = reg.a
		j = reg.b

		if i == j :
			self.view.sel().add(self.view.word(reg))
			return

		if i > 1 :
			i = self.search('.([{"\'+-', i-2, -1)
		if j < self.view.size()-1 :
			j = self.search('.)]}"\'+-', j+1, 1)

		self.view.sel().add(sublime.Region(i, j))

	def search(self, chars, start, step) :
		i = start
		while 1 :
			for char in chars :
				if self.view.substr(i-1) == char or i == 0 or i == self.view.size() :
					return i;
			i = i+step


class ClickDetector(sublime_plugin.EventListener) :
	def __init__(self) :
		self.time = time.time()
	def on_text_command(self, view, name, args) :
		sublime.status_message(view.settings().get('syntax'))
		if view.settings().get('syntax').find('Find Results') == -1 :
			if name == 'drag_select':
				thing = time.time() - self.time
				self.time = time.time()
				if thing < .5:
					return ('mathematica_click_select')
