import time

leaders = {
    'people': "Aaron Kimball",
    'elites': "The Barons",
    'ruler': "Allgood Murphy",
    'intel': "Grant C. Hayes",
    }

coup = ""
curr_lead = leaders['people']
new_lead = ""

# This sets up the possible leaders, and their ideals.

def possib():
    for k, v in leaders.items():
        print("%s: %s" %(k, v))
        time.sleep(.25)

# Prints the dictionary in a fashionable method.


def coup():
    while True:
        new_lead = input()
        if new_lead.lower() == "people":
            return leaders['people']
        elif new_lead.lower() == "elites":
            return leaders['elites']
        elif new_lead.lower() == "ruler":
            return leaders['ruler']
        elif new_lead.lower() == "intel":
            return leaders['intel']
        else:
            print("That's not a choice!")

# Coup function, allows you to switch out who the current leader is.

def pos_coup():
    print("For this effect to take place, a coup must be held!")

# Tells the 'player' that for the switch to work, they need to host a coup.

def lead():
    print("Current Leader: " + curr_lead)

# Prints the current leader.

def sep():
    print()
    print("-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-")
    print()

# Simple seperator, used a lot.

def switch():
    print("Would you like to change out the leaders? [Y/N]")
    sec_op = input()
    if sec_op.lower != "n":
        possib()
        print("Who should be changed?")
        ter_op = input()
        print("Who should be put in charge?")
        switch_two(ter_op)
    else:
        pass

#The first part, where it asks you which party to switch out


def switch_two(ter_op):
    if ter_op.lower() == "people":
        switch_people = input()
        leaders.update({'people': switch_people})
        pos_coup()
    elif ter_op.lower() == "elites":
        switch_elites = input()
        leaders.update({'elites': switch_elites})
        pos_coup()
    elif ter_op.lower() == "ruler":
        switch_ruler = input()
        leaders.update({'ruler': switch_ruler})
        pos_coup()
    elif ter_op.lower() == "intel":
        switch_intel = input()
        leaders.update({'intel': switch_intel})
        pos_coup()
    else:
        print("That's not an option!")

# This is the second part of Switch, where it creates a new name for
# a current party.

while True:
    time.sleep(.25)
    lead()
    sep()
    time.sleep(.25)
    print("Would you like to stage a coup? [Y/N]")
    tf = input()
    if tf.lower() == "y":
        time.sleep(.5)
        print("Who would you like to put in charge?")
        time.sleep(1)
        possib()
        curr_lead = coup()
        time.sleep(1)
        print("The coup was successful!")
        sep()
    elif tf.lower() == "n":
        switch()
        print("Would you like to go back? [Y/N]")
        quad_op = input()
        if quad_op.lower() == "y":
            sep()
        else:
            break
            exit
    else:
        print("It's a yes or no question, it's not that hard.")
        sep()
                









        
              
