import sublime_plugin
import sublime
import os
import json
RuleRepository="D:\\Documents\\Rules\\"

ScriptDirectory=os.path.dirname(os.path.realpath(__file__))

class RuleHelper(sublime_plugin.EventListener):
  
    def on_pre_save_async(view, self):
        j_output={}
        j_output['scope']='source.json' 
        words = []
        print ('start')
        for folder in ["Properties","Dataviews","Lookups"]:
            for root, dirs, files in os.walk(RuleRepository+"rules\\"+folder):
                for file in files:
                    if file.endswith(".json"):
                        with open(os.path.join(root,file), 'r',encoding="utf8") as f: 
                            try:
                                field=json.load(f)
                                Description=field['Description']
                            except Exception:
                                Description='Bad Json' 
                        words.append(file.replace(".json","")+'\t    '+folder+" : "+Description) 

        j_output['completions'] = [{'trigger': w, 'contents':w[:str(w).find("\t")]} for w in words]
        
        with open(ScriptDirectory+'\\rapptr.sublime-completions','w+') as output:
            json.dump(j_output, output,indent=4)
        
