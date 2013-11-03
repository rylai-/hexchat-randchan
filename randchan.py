import string
import random
import xchat as HC

__module_name__ = "HexChat random channel plugin"
__module_version__ = "0.0.1"
__module_description__ = "randchan cmd"
__author__ = "Rylee Elise Fowler"

def randchan (length=10):
    try:
        HC.command('join' + ''.join(random.sample(string.lowercase, 10))
    except:
        print('error: this failed somehow')

HC.hook_command("randchan", randchan)
HC.prnt(__module_name__ + ' version ' + __module_version__ + ' loaded.')
