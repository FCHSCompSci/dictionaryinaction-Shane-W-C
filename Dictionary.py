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

#This sets up the possible leaders, and their ideals.

def possib():
    for k, v in leaders.items():
        print("%s, %s" %(k, v))
        time.sleep(.25)


def coup():
    while True:
        new_lead = input()
        if new_lead.lower() == "people":
            curr_lead = leaders['people']
            break
        elif new_lead.lower() == "elites":
            curr_lead = leaders['elites']
            break
        elif new_lead.lower() == "ruler":
            curr_lead = leaders['ruler']
            break
        elif new_lead.lower() == "intel":
            curr_lead = leaders['intel']
            break
        else:
            print("That's not a choice!")

def lead():
    print("Current Leader: " + curr_lead)

def sep():
    print()
    print("-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-")
    print()

def switch():
    print("Would you like to change out the leaders? [Y/N]")
    sec_op = input()
    if sec_op.lower != "n":
        possib()
        print("Who should be changed?")
        ter_op = input()
        switch_two(ter_op)
    else:
        pass


def switch_two(ter_op):
    if ter_op.lower() == "people":
        leaders['people'] = input()
    elif ter_op.lower() == "elites":
        leaders['elites'] = input()
    elif ter_op.lower() == "ruler":
        leaders['ruler'] = input()
    elif ter_op.lower() == "intel":
        leaders['intel'] = input()
    else:
        print("That's not an option!")

# Setting up my Functions

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
        coup()
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
                









        
              
