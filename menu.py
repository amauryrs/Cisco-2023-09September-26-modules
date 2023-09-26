def menu(*args):   # any number of positional arguments; args is then a tuple containing them
    while True:
        s = input(f'Enter choice ({args}): ').strip()
    
        if s in args:
            return s     # did the user choose one of the elements of args? Return it!

        print(f'{s} is not a valid option; try again!')

# were we run interactively, and *NOT* imported?
# give the user a demo of our menu function!
if __name__ == '__main__':
    user_choice = menu