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
    new_actions = ['place_street_road', 'increase_workforce', 'sell_images', 'won_level', 'place_market']  #all unique possible actions
    action_stream = ['place_street_road', 'increase_workforce', 'sell_images', 'won_level', 'place_street_road', 'place_market', 'increase_workforce']
    #store fired actions (if fired multiple times archive instances as dummyobjects)
    fired_actions = {}

    #store chunk activations after every action 
    chunk_activations = {}

    focus=Buffer()

    DMBuffer=Buffer()  
    # latency controls the relationship between activation and recall  
    # activation must be above threshold - can be set to none               
    DM=Memory(DMBuffer,latency=0.05,threshold=0.5)      
                                                     
    # turn on for DM subsymbolic processing      
    dm_n=DMNoise(DM,noise=0.0,baseNoise=0.0)   
    # turn on for DM subsymbolic processing
    dm_bl=DMBaseLevel(DM,decay=0.5,limit=None) 

    def init():
        focus.set('action_0')      
    
    
    
    
    def action_0(focus='action_0'):
        countHelper = -1
        if (action_stream[len(fired_actions)] in new_actions):
            new_actions.remove(action_stream[len(fired_actions)])
            dmstring = 'action_0:' + action_stream[len(fired_actions)]
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

        

    def forgot_0(focus='action_0_', DMBuffer=None, DM='error:True'):
        # DMBuffer=none means the buffer is empty
        # DM='error:True' means the search was unsucessful
        print ("I forgot something")
        focus.set('stop')
        self.print_activations()

    def remember_0(focus='action_0_', DMBuffer="action_0:?action"):
        # DMBuffer=none means the buffer is empty
        # DM='error:True' means the search was unsucessful
        print ("I remember action_0:",action)
        if len(action_stream) == len(fired_actions) :
            focus.set('stop')
        else : 
            DM.add('action_0:?action')      
            fired_actions[action_stream[len(fired_actions)]]= str(len(fired_actions))
            fired_actions['dummy_0'] = action_stream[len(fired_actions)]
            focus.set('action_' + str(len(fired_actions)))
        self.print_activations()


    def action_1(focus='action_1'):
        countHelper = -1
        if (action_stream[len(fired_actions)] in new_actions):
            new_actions.remove(action_stream[len(fired_actions)])
            dmstring = 'action_1:' + action_stream[len(fired_actions)]
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

        

    def forgot_1(focus='action_1_', DMBuffer=None, DM='error:True'):
        # DMBuffer=none means the buffer is empty
        # DM='error:True' means the search was unsucessful
        print ("I forgot something")
        focus.set('stop')
        self.print_activations()

    def remember_1(focus='action_1_', DMBuffer="action_1:?action"):
        # DMBuffer=none means the buffer is empty
        # DM='error:True' means the search was unsucessful
        print ("I remember action_1:",action)
        if len(action_stream) == len(fired_actions) :
            focus.set('stop')
        else : 
            DM.add('action_1:?action')      
            fired_actions[action_stream[len(fired_actions)]]= str(len(fired_actions))
            fired_actions['dummy_1'] = action_stream[len(fired_actions)]
            focus.set('action_' + str(len(fired_actions)))
        self.print_activations()


    def action_2(focus='action_2'):
        countHelper = -1
        if (action_stream[len(fired_actions)] in new_actions):
            new_actions.remove(action_stream[len(fired_actions)])
            dmstring = 'action_2:' + action_stream[len(fired_actions)]
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

        

    def forgot_2(focus='action_2_', DMBuffer=None, DM='error:True'):
        # DMBuffer=none means the buffer is empty
        # DM='error:True' means the search was unsucessful
        print ("I forgot something")
        focus.set('stop')
        self.print_activations()

    def remember_2(focus='action_2_', DMBuffer="action_2:?action"):
        # DMBuffer=none means the buffer is empty
        # DM='error:True' means the search was unsucessful
        print ("I remember action_2:",action)
        if len(action_stream) == len(fired_actions) :
            focus.set('stop')
        else : 
            DM.add('action_2:?action')      
            fired_actions[action_stream[len(fired_actions)]]= str(len(fired_actions))
            fired_actions['dummy_2'] = action_stream[len(fired_actions)]
            focus.set('action_' + str(len(fired_actions)))
        self.print_activations()


    def action_3(focus='action_3'):
        countHelper = -1
        if (action_stream[len(fired_actions)] in new_actions):
            new_actions.remove(action_stream[len(fired_actions)])
            dmstring = 'action_3:' + action_stream[len(fired_actions)]
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

        

    def forgot_3(focus='action_3_', DMBuffer=None, DM='error:True'):
        # DMBuffer=none means the buffer is empty
        # DM='error:True' means the search was unsucessful
        print ("I forgot something")
        focus.set('stop')
        self.print_activations()

    def remember_3(focus='action_3_', DMBuffer="action_3:?action"):
        # DMBuffer=none means the buffer is empty
        # DM='error:True' means the search was unsucessful
        print ("I remember action_3:",action)
        if len(action_stream) == len(fired_actions) :
            focus.set('stop')
        else : 
            DM.add('action_3:?action')      
            fired_actions[action_stream[len(fired_actions)]]= str(len(fired_actions))
            fired_actions['dummy_3'] = action_stream[len(fired_actions)]
            focus.set('action_' + str(len(fired_actions)))
        self.print_activations()


    def action_4(focus='action_4'):
        countHelper = -1
        if (action_stream[len(fired_actions)] in new_actions):
            new_actions.remove(action_stream[len(fired_actions)])
            dmstring = 'action_4:' + action_stream[len(fired_actions)]
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

        

    def forgot_4(focus='action_4_', DMBuffer=None, DM='error:True'):
        # DMBuffer=none means the buffer is empty
        # DM='error:True' means the search was unsucessful
        print ("I forgot something")
        focus.set('stop')
        self.print_activations()

    def remember_4(focus='action_4_', DMBuffer="action_4:?action"):
        # DMBuffer=none means the buffer is empty
        # DM='error:True' means the search was unsucessful
        print ("I remember action_4:",action)
        if len(action_stream) == len(fired_actions) :
            focus.set('stop')
        else : 
            DM.add('action_4:?action')      
            fired_actions[action_stream[len(fired_actions)]]= str(len(fired_actions))
            fired_actions['dummy_4'] = action_stream[len(fired_actions)]
            focus.set('action_' + str(len(fired_actions)))
        self.print_activations()


    def action_5(focus='action_5'):
        countHelper = -1
        if (action_stream[len(fired_actions)] in new_actions):
            new_actions.remove(action_stream[len(fired_actions)])
            dmstring = 'action_5:' + action_stream[len(fired_actions)]
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

        

    def forgot_5(focus='action_5_', DMBuffer=None, DM='error:True'):
        # DMBuffer=none means the buffer is empty
        # DM='error:True' means the search was unsucessful
        print ("I forgot something")
        focus.set('stop')
        self.print_activations()

    def remember_5(focus='action_5_', DMBuffer="action_5:?action"):
        # DMBuffer=none means the buffer is empty
        # DM='error:True' means the search was unsucessful
        print ("I remember action_5:",action)
        if len(action_stream) == len(fired_actions) :
            focus.set('stop')
        else : 
            DM.add('action_5:?action')      
            fired_actions[action_stream[len(fired_actions)]]= str(len(fired_actions))
            fired_actions['dummy_5'] = action_stream[len(fired_actions)]
            focus.set('action_' + str(len(fired_actions)))
        self.print_activations()


    def action_6(focus='action_6'):
        countHelper = -1
        if (action_stream[len(fired_actions)] in new_actions):
            new_actions.remove(action_stream[len(fired_actions)])
            dmstring = 'action_6:' + action_stream[len(fired_actions)]
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

        

    def forgot_6(focus='action_6_', DMBuffer=None, DM='error:True'):
        # DMBuffer=none means the buffer is empty
        # DM='error:True' means the search was unsucessful
        print ("I forgot something")
        focus.set('stop')
        self.print_activations()

    def remember_6(focus='action_6_', DMBuffer="action_6:?action"):
        # DMBuffer=none means the buffer is empty
        # DM='error:True' means the search was unsucessful
        print ("I remember action_6:",action)
        if len(action_stream) == len(fired_actions) :
            focus.set('stop')
        else : 
            DM.add('action_6:?action')      
            fired_actions[action_stream[len(fired_actions)]]= str(len(fired_actions))
            fired_actions['dummy_6'] = action_stream[len(fired_actions)]
            focus.set('action_' + str(len(fired_actions)))
        self.print_activations()




    def action_7(focus = 'action_7'): 
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

 