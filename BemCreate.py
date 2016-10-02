import sublime, sublime_plugin
import json
from os.path import dirname, realpath, join, expanduser

try:
	# Python 2
	from node_bridge import node_bridge
except:
	from .node_bridge import node_bridge

BIN_PATH = join(sublime.packages_path(), dirname(realpath(__file__)), 'bem-create-provider.js')

class BemCreateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# Execute code with node.js
		def node_exec(data):
			try:
				node_bridge(data, BIN_PATH)
			except Exception as e:
				sublime.error_message('bem-create\n%s' % e)
		# Show input panel and get data from user, then use callback.
		def getData():
			extract_variables = self.view.window().extract_variables()
			file_path = extract_variables.get('file')
			file_name = extract_variables.get('file_name')
			folder_path = file_path[:-len(file_name)] if file_name is not None else ''
			home_directory = expanduser('~')
			config_default = "{\"block\":{\"block\":\"khvostov\"},\"paths\":[\"%s\"],\"techs\":[\"css\",\"js\", \"bemjson\"]}" % (folder_path or home_directory)
			self.view.window().show_input_panel('Block name, path, techs', config_default, node_exec, None, None)

		getData()