import sublime, sublime_plugin
import json
from os.path import dirname, realpath, join

try:
	# Python 2
	from node_bridge import node_bridge
except:
	from .node_bridge import node_bridge

BIN_PATH = join(sublime.packages_path(), dirname(realpath(__file__)), 'bem-tools-provider.js')

class BemToolsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		settings = {
			'block': [
				{ 'block': "vitaly", "elem": "e2" },
				{ 'block': 'vitaly', 'elem': 'e2', 'modName': 'elemMod', 'modVal': 'true' },
				{ 'block': 'vlad'}
			],
			'paths': ['C:/sublime/Data/Packages/BemTools'],
			'techs': ["css", "js"]
		}
		convertToJson = json.dumps(settings)
		try:
			node_bridge(convertToJson, BIN_PATH)
		except Exception as e:
			sublime.error_message('bem-create\n%s' % e)
