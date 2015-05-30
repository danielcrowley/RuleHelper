# Extends Sublime Text autocompletion to find matches in all open
# files. By default, Sublime only considers words from the current file.

import sublime_plugin
import sublime
import os
RuleRepository="D:\\Documents\\Rules\\"
class RuleHelper(sublime_plugin.EventListener):
    
    def on_query_completions(self, view, prefix, locations):
        words = []

        for folder in ["Properties","DataViews","Lookups"]:
            for root, dirs, files in os.walk(RuleRepository+"rules\\"+folder):
                for file in files:
                    if file.endswith(".json"):
                        words.append(file.replace(".json",""))
        print (words)

        matches = [(w, w.replace('$', '\\$')) for w in words]
        return matches


if sublime.version() >= '3000':
  def is_empty_match(match):
    return match.empty()
else:
  def is_empty_match(match):
    return match is None
