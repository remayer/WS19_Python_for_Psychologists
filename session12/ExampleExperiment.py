#!/usr/bin/python
#-- coding: UTF-8 --
##### Experiment adapted from: 
## Nehler, K. J. & Sassenhagen, J. (2020). DRM-Paradigm with Psychopy: An in-depth look at Programming Experiments. In S.E.P. Boettcher, D. Draschkow, J. Sassenhagen & M. Schultze (Eds.). *Scientific Methods for Open Behavioral, Social and Cognitive Sciences*. https://doi.org/10.17605/OSF.IO/M2YDS



from __future__ import unicode_literals, print_function, division   #importing external functions but only the functions that are used in the experiment, important because Psychopy programms in Python 2 not 3
from random import shuffle
from random import choice
from psychopy import visual, event, core, monitors #Psychopy Basis modules for presentation (Quellenangaben nicht vergessen!), waitkeys und TextStim sind Funktionen in event


########## STUFF YOU WILL NEED AT SOME POINT ############################################################################################

################################
#### Complete stimulus list ####
################################
stim_list = {"1chair": ["table", "sit", "legs", "couch", "sofa", "wood", "cushion", "bench", "sit", "stool"],
             "2cold": ["hot", "snow", "warm", "winter", "ice", "wet", "frigid", "chilly", "heat", "weather"],
             "3fruit": ["apple", "vegetable", "orange", "kiwi", "juice", "pear", "banana", "ripe", "cocktail", "bowl"],
             "4_1future": ["real estate agent","process automation specialist","trainer","developer","social media manager","e-commerce manager","solutions designer","data analyst","big data specialist","robotics engineer"],
             "4_2past": ["assembly-line worker","tailor","car driver","construction worker","carpenter","door-to-door sales worker","shoemaker","scaffolding worker","smith","glassblower"],
             "5mountain": ["hill", "valley", "climb", "peak", "goat", "bike", "climber", "ski", "steep", "plain"],
             "6music": ["note", "piano", "sing", "radio", "band", "melody", "horn", "concert", "instrument", "symphony"],
             "7sleep": ["bed", "rest", "awake", "tired", "dream", "wake", "snooze", "blanket", "doze", "slumber"]} #Dictionary, Value pairs seperated by comma

###################################
#### Define long text elements ####
###################################

task_description = """
In this experiment your memory capacity will be tested.

The experiment is seperated into different parts. 
In the first part you will be presented different words to learn.
Later you will be asked to recognize the learned words.

Press any key to continue.
"""

instruction_codegeneration = """
Please generate your personal code.

Enter the following characters in a row:
- 1. and 2. letter of your mother's first name (Anna -> "AN")
- Your month of birth (May -> "05") 
- 1. and 2. letter of your father's first name (Marvin -> "MA") 

Press 'Enter' to proceed.
"""

instruction_learning = """
Now you will be presented a lot of words.
Try to remember as many words as you can. 

Press any key to start.
"""

proceed_text = "Please press 'Enter' to continue with the next part of the experiment."



############################ YOUR TASKS ####################################################################################


######################
#### Define clock ####
######################
#### TASK 1: Define a clock called "clocki" and a fullscreen window called "win". 
clocki = core.Clock() 


#################################
#### Define monitor & window ####
#################################
m = monitors.Monitor("test", width=28.8, distance=90, autoLog=True)
m.setSizePix([1024, 800])
win = visual.Window(monitor=m, units='pix', winType='pyglet', fullscr=True) 


#########################
#### Define exit key ####
#########################
#### TASK 2: Have the experiment stop if "ESC" is pressed.
event.globalKeys.clear()
event.globalKeys.add(key="escape", func=core.quit)


##################################################
#### Randomly assign subject to one condition ####
##################################################
#### Task 3: Create a variable "condition" that contains the result of a random choice of an item in the list ["past", "future"]. 
condition = choice(["past", "future"])


####################################################
#### Reduce stimulus set according to condition ####
####################################################
#### Task 4: Depending on the condition, delete the elements "4_1future" OR "4_2past" from the stimulus dictionary "stim_list". 
if condition == "future":
    del stim_list[("4_2past")]
elif condition == "past":
    del stim_list[("4_1future")]


#############################################
#### Create ONE list of stimuli to learn ####
#############################################
#### Task 5: Now, create a new empty list "learn_stims" which will (eventually) contain all stimuli that subjects will be presented during the learning phase.
####         For that aim you will have to combine all stimulus lists contained in the dictionary "stim_list" in your new list "learn_stims". Finally, shuffle the list
####         "learn_stims".
learn_stims = []
for list in stim_list.values():
    learn_stims.extend(list)
shuffle(learn_stims)





##-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
##-#-#-# START EXPERIMENTAL PROCEDURE  #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
##-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#


##################################
#### Present task_description ####
##################################
#### Task 7: Now it is time to present the initial "task_description" text. After presenting the text on the screen, use "waitKeys" to present the screen until a response is made.
visual.TextStim(win, task_description).draw() 
win.flip() 
event.waitKeys()


#######################################
#### Present code generator screen ####
#######################################
#### Task 8: The subjects in this experiment will have to generate a personal code as their subject ID. The instructions for this are stored in "instruction_codegeneration" above.
####         For that aim we will need to 
def text_writer(msg): 
    chars = []

    visual.TextStim(win, msg, pos=(0, -200)).draw()
    win.flip()

    while True:
        visual.TextStim(win, msg, pos=(0, -200)).draw()
        key = event.waitKeys()[0].lower()
        if key in ("return", "enter"):
            break
        elif key == "backspace":
            chars = chars[:-1]
        elif key in "abcdefghijklmnopqrstuvwxyz0123456789":
            chars.append(key)
        else:
            continue
        new_code = "".join(chars).upper()
        visual.TextStim(win, new_code).draw()
        win.flip()
    win.flip()
    return chars



##########################################
#### Generate and assign subject code ####
##########################################
#### TASK 9: Call text_writer() function and pass it the "instruction_codegeneration" as a message. As you know, the text_writer() function, apart from presenting the 
####         code generation screen, also has a return value (i.e., the generated code itself), we can assign this return value to a variable. Assign the function's return value
####         to a variable called "subject_ID".
subject_ID = text_writer(instruction_codegeneration)





####################################
#### Present the "proceed_text" ####
####################################
#### TASK 10: Present the "proceed_text" on the screen. Then, wait for the subejct to press "return" or "enter" (argument "keyList"). Finally, create a function called 
####          "proceed_screen()" out of your code, and call the function to present the proceed_screen. 
def proceed_screen():
    visual.TextStim(win, proceed_text).draw() 
    win.flip() 
    event.waitKeys(keyList = ["return", "enter"]) 
proceed_screen()





#####################################################
#### Present a short break before stimulus onset ####
#####################################################
visual.TextStim(win, "").draw() 
win.flip() 
core.wait(2)





#########################################
#### Present words in learning phase ####
#########################################
#### TASK 11: Now, fill in the "show_words()" function. Afterwards create a loop presenting all the words contained in learn_stims using the new show_words() function.
def show_words(text, phase):
    word = visual.TextStim(win, text)
    word.draw()
    if phase == "learning": # for now we are only concentrating on the learning phase
        win.flip()
        core.wait(0.2) # speeded up a lot for testing purposes (should be 0.5 s)


for stim in learn_stims:
    show_words(text=stim,phase="learning")



######################
#### Close window ####
######################
win.close()








