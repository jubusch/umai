import sys
sys.path.insert(0, 'ccmsuite')

import ccm
from ccm.lib.actr import *
import global_variables
log=ccm.log()

class MyEnvironment(ccm.Model):
    """
    TODO documentation
    """
    pass

class MyAgent(ACTR):
    """
    TODO documentation
    """
    new_actions = ${new_actions}  #all unique possible actions
    
    
    
    ${actions_methods}

## ...
 