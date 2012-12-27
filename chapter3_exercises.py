# Exercises for chapter 3: Problems 3.1, 3.2, 3.3, and 3.4 in Think Python

# chrisvans - Chris Van Schyndel

# 3.1

# NameError: name 'repeat_lyrics' is not defined

# 3.2

# The program runs properly.  Function order does not matter, as long as it
# is defined before it is called.

# 3.3


def right_justify(s):
    if s == str(s):
        print ' ' * 70 + s
    else:
        print 'Input must be a string!'
        
right_justify("bagel")

# 3.4

def do_twice(f, s):
    f(s)
    f(s)
    
def print_spam():
    print 'spam'
    
def print_twice(message):
    print message
    print message
    
do_twice(print_twice, 'spam')  

def do_four(function, value):
    do_twice(function, value)
    do_twice(function, value)
    
do_four(print_twice, 'spam')