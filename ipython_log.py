# IPython log file


# simple example

import random              # imported the "random" module
random.randint(0, 100)     # invoked the randint function defined in the random module, passing it 0 and 100
type(random)
# you cannot have a module "random" and also a function "random" and also a variable "random"
# there can be only one value assigned to the "random" variable at any given time!
# the latest one that was defined works and sticks around... the others are gone

type(random)
# what names are defined? We imported the module to get functions, objects, and data
# what did we get?

# we can use the "dir" function on our module to get a list of its attributes, names that come after a .
# dir won't tell us the type of value on each attribute, but it will tell us what was defined.

dir(random)
import sys  # because it's already loaded, we just define the name here with this statement
sys.path     # this is a list of strings, directories in which Python will look for a module
random
import abcde
import random
type(random)
random = 6
type(random)
import random
type(randoM)
type(random)
sys.modules
'random' in sys.modules
'rich' in sys.modules
import rich
'rich' in sys.modules
rich = 6
type(rich)
'rich' in sys.modules
import random
randint(0, 3)
from random import randint
del(random)  # get rid of the module variable
from random import randint
dir(random)
sys
get_ipython().run_line_magic('time', '')
import time
time
import re
dir(re)
import re
from re import findall as refa
refa('asdfa')
import mymod
dir(mymod)   
mymod.__file__
mymod.__name__
import mymod
dir(mymod)
# normally, when you import a module a second time in a program (or in Jupyter),
# you don't get it reloaded automatically.  I actually did set things to reload...

# normally, if you want to reload a module, you need to grab the "reload" function from the "importlib" module
from importlib import reload
reload(mymod)
mymod.x
mymod.y
mymod.hello('out there')
import menu
user_choice = menu.menu('a', 'b', 'c')

print(f'The user chose {user_choice}.')
import menu
user_choice = menu.menu('a', 'b', 'c')

print(f'The user chose {user_choice}.')
import menu
user_choice = menu.menu('a', 'b', 'c')

print(f'The user chose {user_choice}.')
reload(mymod)
