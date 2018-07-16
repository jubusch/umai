from string import Template
from io import StringIO
import global_variables

action_tpl = """
    def action_${action_nr}(focus='action_${action_nr}'):
        countHelper = -1
        if (action_stream[len(fired_actions)] in new_actions:
            pass
"""

actions_methods_stream = StringIO()
for i,x in enumerate(global_variables.action_stream):
    actions_methods_stream.write(Template(action_tpl).substitute(action_nr=i))
    actions_methods_stream.write('\n')


    
with open('simulation.tpl') as fin:
    tpl = fin.read()
content_substituted = Template(tpl).substitute(new_actions=global_variables.new_actions, actions_methods=actions_methods_stream.getvalue())

with open('simulation2.py', 'w') as fout:
    fout.write(content_substituted)
