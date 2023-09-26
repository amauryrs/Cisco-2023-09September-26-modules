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
