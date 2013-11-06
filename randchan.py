import string
import random
import xchat

__module_name__ = "HexChat random channel plugin"
__module_version__ = "0.0.1"
__module_description__ = "randchan cmd"
__author__ = "Rylee Elise Fowler"

def randchan (word, word_eol, userdata):
    xchat.command('join #' + ''.join(random.sample(string.ascii_lowercase, 10)))

xchat.hook_command("randchan", randchan)
xchat.prnt(__module_name__ + ' version ' + __module_version__ + ' loaded.')
