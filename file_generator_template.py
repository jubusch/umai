from string import Template
from io import BytesIO
import global_variables

action_tpl = """
    def action_${action_nr}(focus='action_${action_nr}'):
        countHelper = -1
        if (action_stream[len(fired_actions)] in new_actions):
            new_actions.remove(action_stream[len(fired_actions)])
            dmstring = 'action_${action_nr}:' + action_stream[len(fired_actions)]
            fired_actions[action_stream[len(fired_actions)]]= str(len(fired_actions))
            DM.add(dmstring)
            #print count
            #count = count + 1 
            focus.set('action_' + str(len(fired_actions)))
        else : 
            countHelper = 0
            dmstring = 'action_' + fired_actions[action_stream[len(fired_actions)]] + ':?action'
            DM.request(dmstring) 
            focus.set('action_' + fired_actions[action_stream[len(fired_actions)]] + '_')
        #store activations
        #can't acces chunk_activation in print_activation function
        list_of_chunks = self.DM.find_matching_chunks('')
        actions_temp = [str(i).split(':')[0] for i in list_of_chunks]
        #chunk_activations[str(len(fired_actions)-1)]={str(chunk[actions_temp[i]]) : str(round(self.DM.get_activation(chunk), 3)) for i,chunk in enumerate(list_of_chunks)}
        self.print_activations()
        chunk_activations[str(len(fired_actions)+countHelper)] = {}
        for i,chunk in enumerate(list_of_chunks):
            #print(i,chunk, actions_temp[i], chunk[actions_temp[i]], str(chunk[actions_temp[i]]))
            chunk_activations[str(len(fired_actions)+countHelper)][str(chunk[actions_temp[i]])] = str(round(self.DM.get_activation(chunk), 3))
        print chunk_activations

        

    def forgot_${action_nr}(focus='action_${action_nr}_', DMBuffer=None, DM='error:True'):
        # DMBuffer=none means the buffer is empty
        # DM='error:True' means the search was unsucessful
        print ("I forgot something")
        focus.set('stop')
        self.print_activations()

    def remember_${action_nr}(focus='action_${action_nr}_', DMBuffer="action_${action_nr}:?action"):
        # DMBuffer=none means the buffer is empty
        # DM='error:True' means the search was unsucessful
        print ("I remember action_${action_nr}:",action)
        if len(action_stream) == len(fired_actions) :
            focus.set('stop')
        else : 
            DM.add('action_${action_nr}:?action')      
            fired_actions[action_stream[len(fired_actions)]]= str(len(fired_actions))
            fired_actions['dummy_${action_nr}'] = action_stream[len(fired_actions)]
            focus.set('action_' + str(len(fired_actions)))
        self.print_activations()
"""

actions_methods_stream = BytesIO()
for i,x in enumerate(global_variables.action_stream):
    actions_methods_stream.write(Template(action_tpl).substitute(action_nr=i))
    actions_methods_stream.write('\n')
    
    	


    
with open('simulation.tpl') as fin:
    tpl = fin.read()
content_substituted = Template(tpl).substitute(last_action = len(global_variables.action_stream),new_actions=global_variables.new_actions,action_stream=global_variables.action_stream,noise=global_variables.noise,baseNoise=global_variables.baseNoise,latency=global_variables.latency,threshold=global_variables.threshold,decay=global_variables.decay, actions_methods=actions_methods_stream.getvalue())

with open('simulation.py', 'w') as fout:
    fout.write(content_substituted)
