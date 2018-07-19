import sys
sys.path.insert(0, 'ccmsuite')

import ccm
from ccm.lib.actr import *
import global_variables
log=ccm.log()

class MyEnvironment(ccm.Model):
    pass

class MyAgent(ACTR):
    """
    TODO documentation
    """
    new_actions = ${new_actions}  #all unique possible actions
    action_stream = ${action_stream}
    #store fired actions (if fired multiple times archive instances as dummyobjects)
    fired_actions = {}

    #store chunk activations after every action 
    chunk_activations = {}

    focus=Buffer()

    DMBuffer=Buffer()  
    # latency controls the relationship between activation and recall  
    # activation must be above threshold - can be set to none               
    DM=Memory(DMBuffer,latency=${latency},threshold=${threshold})      
                                                     
    # turn on for DM subsymbolic processing      
    dm_n=DMNoise(DM,noise=${noise},baseNoise=${baseNoise})   
    # turn on for DM subsymbolic processing
    dm_bl=DMBaseLevel(DM,decay=${decay},limit=None) 

    def init():
        focus.set('action_0')      
    
    
    
    ${actions_methods}


    def action_${last_action}(focus = 'action_${last_action}'): 
       	focus.set('stop')
        
    def stop_production(focus = 'stop'):
        self.stop()

    def print_activations(self):
        list_of_chunks = self.DM.find_matching_chunks('')
        actions = [str(i).split(':')[0] for i in list_of_chunks]
        print "\nCurrent chunk activation values:"
        print "--------------------------------"
        print list_of_chunks
        #print self.DM.get_activation()
        for i,chunk in enumerate(list_of_chunks):
                #chunk_activations[str(chunk[actions[i]])]= str(round(self.DM.get_activation(chunk), 3))
                print chunk[actions[i]], "-->", \
                round(self.DM.get_activation(chunk), 3)
        print "\n"

umai = MyAgent()
umaiEnvironment = MyEnvironment()
umaiEnvironment.agent = umai
ccm.log_everything(umai)
umaiEnvironment.run() 
global_variables.chunk_activations = umai.chunk_activations 
ccm.finished()  

 