import sys
sys.path.insert(0, 'ccmsuite')

import ccm
from ccm.lib.actr import *

import global_variables   
log=ccm.log()   

from ccm.lib.actr import *  

#####
# Python ACT-R requires an environment
# but in this case we will not be using anything in the environment
# so we 'pass' on putting things in there



class MyEnvironment(ccm.Model):
    pass

#####
# create an act-r agent

class MyAgent(ACTR):

    #array represents all new actions 
    new_actions = ['place_street_road','increase_workforce','sell_images','won_level', 'place_market']
    #actions_stream comes in via rest
    action_stream = ['place_street_road','increase_workforce','sell_images','won_level','place_street_road', 'place_market','increase_workforce']
    #store all fired actions
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


    # turn on spreading activation for DM from focus
    dm_spread = DMSpreading(DM, focus)
    # set strength of activation for buffers
    dm_spread.strength = 2
    # set weight to adjust for how many slots in the buffer
    # usually this is strength divided by number of slots
    dm_spread.weight[focus] = .5

    

    
    def init():
        #print str(len(fired_actions)+1)
        focus.set('action_0')

    
#ation_0
    def action_0(focus='action_0'): 
        # print '#########################################'
        # print 'action_'+str(len(fired_actions))+':'+ action_stream[len(fired_actions)]
        # print str(len(fired_actions))
        # print action_stream
        # print new_actions
        # print fired_actions
        # print str(DMBuffer == None)
        # print '#########################################'
        countHelper = -1
        if (action_stream[len(fired_actions)] in new_actions) : 
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
            #DMbuffer.clear()
            fired_actions[action_stream[len(fired_actions)]]= str(len(fired_actions))
            fired_actions['dummy_0'] = action_stream[len(fired_actions)]
            focus.set('action_' + str(len(fired_actions)))
        self.print_activations()

#ation_1
    def action_1(focus='action_1'): 
        # print '#########################################'
        # print 'action_'+str(len(fired_actions))+':'+ action_stream[len(fired_actions)]
        # print str(len(fired_actions))
        # print action_stream
        # print new_actions
        # print fired_actions
        # print str(DMBuffer == None)
        # print '#########################################'
        countHelper = -1
        if (action_stream[len(fired_actions)] in new_actions) : 
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
        self.print_activations()
        list_of_chunks = self.DM.find_matching_chunks('')
        actions_temp = [str(i).split(':')[0] for i in list_of_chunks]
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
            fired_actions['dummy_1'] = 'dummyElement'
            focus.set('action_' + str(len(fired_actions)))
        self.print_activations()

#ation_2
    def action_2(focus='action_2'): 
        # print '#########################################'
        # print 'action_'+str(len(fired_actions))+':'+ action_stream[len(fired_actions)]
        # print str(len(fired_actions))
        # print action_stream
        # print new_actions
        # print fired_actions
        # print str(DMBuffer == None)
        # print '#########################################'
        countHelper = -1
        if (action_stream[len(fired_actions)] in new_actions) : 
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
        self.print_activations()
        list_of_chunks = self.DM.find_matching_chunks('')
        actions_temp = [str(i).split(':')[0] for i in list_of_chunks]
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
            fired_actions[action_stream[len(fired_actions)]]= str(len(fired_actions))
            fired_actions['dummy_2'] = 'dummyElement'
            focus.set('action_' + str(len(fired_actions)))
        self.print_activations()

#ation_3
    def action_3(focus='action_3'): 
        print '#########################################'
        print 'action_'+str(len(fired_actions))+':'+ action_stream[len(fired_actions)]
        print str(len(fired_actions))
        print action_stream
        print new_actions
        print fired_actions
        print str(DMBuffer == None)
        print '#########################################'
        countHelper = -1
        if (action_stream[len(fired_actions)] in new_actions) : 
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
        self.print_activations()
        list_of_chunks = self.DM.find_matching_chunks('')
        actions_temp = [str(i).split(':')[0] for i in list_of_chunks]
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
            fired_actions[action_stream[len(fired_actions)]]= str(len(fired_actions))
            fired_actions['dummy_3'] = 'dummyElement'
            focus.set('action_' + str(len(fired_actions)))
        self.print_activations()

#ation_4
    def action_4(focus='action_4'): 
        print '#########################################'
        print 'action_'+str(len(fired_actions))+':'+ action_stream[len(fired_actions)]
        print str(len(fired_actions))
        print action_stream
        print new_actions
        print fired_actions
        print str(DMBuffer == None)
        print '#########################################'
        countHelper = -1
        if (action_stream[len(fired_actions)] in new_actions) : 
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
        self.print_activations()
        list_of_chunks = self.DM.find_matching_chunks('')
        actions_temp = [str(i).split(':')[0] for i in list_of_chunks]
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
            fired_actions[action_stream[len(fired_actions)]]= str(len(fired_actions))
            fired_actions['dummy_4'] = 'dummyElement'
            focus.set('action_' + str(len(fired_actions)))
        self.print_activations()

#ation_5
    def action_5(focus='action_5'): 
        # print '#########################################'
        # print 'action_'+str(len(fired_actions))+':'+ action_stream[len(fired_actions)]
        # print str(len(fired_actions))
        # print action_stream
        # print new_actions
        # print fired_actions
        # print str(DMBuffer == None)
        # print '#########################################'
        countHelper = -1
        if (action_stream[len(fired_actions)] in new_actions) : 
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
        self.print_activations()
        list_of_chunks = self.DM.find_matching_chunks('')
        actions_temp = [str(i).split(':')[0] for i in list_of_chunks]
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
            fired_actions[action_stream[len(fired_actions)]]= str(len(fired_actions))
            fired_actions['dummy_5'] = 'dummyElement'
            focus.set('action_' + str(len(fired_actions)))
        self.print_activations()

#ation_6
    def action_6(focus='action_6'): 
        # print '#########################################'
        # print 'action_'+str(len(fired_actions))+':'+ action_stream[len(fired_actions)]
        # print str(len(fired_actions))
        # print action_stream
        # print new_actions
        # print fired_actions
        # print str(DMBuffer == None)
        # print '#########################################'
        countHelper = -1
        if (action_stream[len(fired_actions)] in new_actions) : 
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
        self.print_activations()
        list_of_chunks = self.DM.find_matching_chunks('')
        actions_temp = [str(i).split(':')[0] for i in list_of_chunks]
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
            fired_actions[action_stream[len(fired_actions)]]= str(len(fired_actions))
            fired_actions['dummy_6'] = 'dummyElement'
            focus.set('action_' + str(len(fired_actions)))
        self.print_activations()

#ation_7
    def action_7(focus='action_7'): 
        if (len(action_stream) == len(fired_actions)) : 
            print '__last production, end of simulation__'
            focus.set('stop')
        self.print_activations()
        list_of_chunks = self.DM.find_matching_chunks('')
        actions_temp = [str(i).split(':')[0] for i in list_of_chunks]
        chunk_activations[str(len(fired_actions))] = {}
        for i,chunk in enumerate(list_of_chunks):
            #print(i,chunk, actions_temp[i], chunk[actions_temp[i]], str(chunk[actions_temp[i]]))
            chunk_activations[str(len(fired_actions))][str(chunk[actions_temp[i]])] = str(round(self.DM.get_activation(chunk), 3))
        print chunk_activations
        #store in values global variables 
        
       



    def stop_production(focus='stop'):
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

        #print chunk_activations 



    def print_production_utilities(self):
        utilities_dict = self.get_activation()
        print "Current production utilities:"
        print "-----------------------------"
        for key, value in utilities_dict.items():
            print key, "-->", round(value, 3)
        print "\n"



        
    # dynamically add functions to MyAgent 
    ##https://artandlogic.com/2015/01/dynamic-python-method/
# def getaction():
#     i = -1; 
#     return ("action_"+ str(i=i+1))
# i = 0;
# def getaction (i) :
#     return "action_%d"%i

# for i,_ in enumerate(action_stream) : 
#     # name = "action_%d"%i
#     if (i+1) == len(action_stream):
#         @staticmethod
#         def action(focus=getaction(i)):
#             # tim.stop() 
#             MyAgent.focus.set('stop')
#     else:
#         @staticmethod
#         def action(focus=getaction(i)):
#             print (focus)
#             MyAgent.focus.set(getaction(i+1))

        ## attach our function here to the instance "agent" (of object MyAgent)
        #setattr(agent, "action_%d" % i, action)
    #setattr(MyAgent, getaction(i), action)
    # i=i+1
    #setattr(MyAgent, getaction(i), action)


tim=MyAgent()                            # name the agent        
# print dir(tim)
# MyAgent.init()
# print MyAgent.focus[0]
#print MyAgent.focus[0]
subway=MyEnvironment()                     # name the environment
subway.agent=tim                           # put the agent in the environment
ccm.log_everything(subway)                 # print out what happens in the environment
#log=ccm.log(html=True)
subway.run()  
global_variables.chunk_activations = tim.chunk_activations  
                          # run the environment FOR 2 SECONDS
ccm.finished()                          # stop the environment
