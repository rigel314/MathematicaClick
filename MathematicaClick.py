import sublime, sublime_plugin, time

class MathematicaClickSelectCommand(sublime_plugin.TextCommand):
	# def __init__(self, view):
	# 	self.view = view
	# 	self.thing = 0
	# 	self.time = time.time()
	def run(self, edit):
		# self.thing = time.time() - self.time
		# self.time = time.time()
		# if self.thing > 1:
		# 	self.thing = 0

		for region in self.view.sel():
			sublime.status_message(str(region.a))

		# if self.thing == 0:
		# 	view.run_command("drag_select")
		# 	sublime.status_message("blar")
		# else:
		# 	sublime.status_message("test"+str(self.thing))

class ClickDetector(sublime_plugin.EventListener):
	def __init__(self):
		self.time = time.time()
	def on_text_command(self, view, name, args):
		if name == 'drag_select':
			thing = time.time() - self.time
			self.time = time.time()
			if thing < 1:
				return ('mathematica_click_select')
