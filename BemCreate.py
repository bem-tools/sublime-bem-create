import sublime, sublime_plugin
import json
from os.path import dirname, realpath, join

try:
	# Python 2
	from node_bridge import node_bridge
except:
	from .node_bridge import node_bridge

BIN_PATH = join(sublime.packages_path(), dirname(realpath(__file__)), 'bem-tools-provider.js')

class BemCreateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# Execute code with node.js
		def node_exec(data):
			try:
				node_bridge(data, BIN_PATH)
			except Exception as e:
				sublime.error_message('bem-create\n%s' % e)
		# Open input and get user data, then use callback.
		self.view.window().show_input_panel('Block name, path, techs', "{\"block\":{\"block\":\"khvostov\"},\"paths\":[\"C:/path/to/ur/proj\"],\"techs\":[\"css\",\"js\", \"bemjson\"]}", node_exec, None, None)

