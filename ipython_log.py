# IPython log file


# simple example

import random              # imported the "random" module
random.randint(0, 100)     # invoked the randint function defined in the random module, passing it 0 and 100
type(random)
# you cannot have a module "random" and also a function "random" and also a variable "random"
# there can be only one value assigned to the "random" variable at any given time!
# the latest one that was defined works and sticks around... the others are gone

type(random)
