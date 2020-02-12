#!/usr/bin/python
#-- coding: UTF-8 --
##### Experiment adapted from: 
## Nehler, K. J. & Sassenhagen, J. (2020). DRM-Paradigm with Psychopy: An in-depth look at Programming Experiments. In S.E.P. Boettcher, D. Draschkow, J. Sassenhagen & M. Schultze (Eds.). *Scientific Methods for Open Behavioral, Social and Cognitive Sciences*. https://doi.org/10.17605/OSF.IO/M2YDS



from __future__ import unicode_literals, print_function, division   
from random import shuffle
from random import choice
from psychopy import visual, event, core, monitors 


########## STUFF YOU WILL NEED AT SOME POINT ############################################################################################

################################################
#### Complete stimulus list (without foils) ####
################################################
stim_list = {"1chair": ["table", "sit", "legs", "couch", "sofa", "wood", "cushion", "bench", "sit", "stool"],
             "2cold": ["hot", "snow", "warm", "winter", "ice", "wet", "frigid", "chilly", "heat", "weather"],
             "3fruit": ["apple", "vegetable", "orange", "kiwi", "juice", "pear", "banana", "ripe", "cocktail", "bowl"],
             "4_1future": ["real estate agent","process automation specialist","trainer","developer","social media manager","e-commerce manager","solutions designer","data analyst","big data specialist","robotics engineer"],
             "4_2past": ["assembly-line worker","tailor","car driver","construction worker","carpenter","door-to-door sales worker","shoemaker","scaffolding worker","smith","glassblower"],
             "5mountain": ["hill", "valley", "climb", "peak", "goat", "bike", "climber", "ski", "steep", "plain"],
             "6music": ["note", "piano", "sing", "radio", "band", "melody", "horn", "concert", "instrument", "symphony"],
             "7sleep": ["bed", "rest", "awake", "tired", "dream", "wake", "snooze", "blanket", "doze", "slumber"]} 

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



##################################################
#### Randomly assign subject to one condition ####
##################################################
#### Task 3: Create a variable "condition" that contains the result of a random choice of an item in the list ["past", "future"]. 



####################################################
#### Reduce stimulus set according to condition ####
####################################################
#### Task 4: Depending on the condition, delete the elements "4_1future" (if condition is "past") OR "4_2past" from the stimulus dictionary "stim_list". 



#############################################
#### Create ONE list of stimuli to learn ####
#############################################
#### Task 5: Now, create a new empty list "learn_stims" which will (eventually) contain all stimuli that subjects will be presented during the learning phase.
####         For that aim you will have to combine all stimulus lists contained in the dictionary "stim_list" in your new list "learn_stims". Finally, shuffle the list
####         "learn_stims".





##-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
##-#-#-# START EXPERIMENTAL PROCEDURE  #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
##-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#


##################################
#### Present task_description ####
##################################
#### Task 7: Now it is time to present the initial "task_description" text. After presenting the text on the screen, use "waitKeys" to present the screen until a response is made.



#######################################
#### Present code generator screen ####
#######################################
#### Task 8: The subjects in this experiment will have to generate a personal code as their subject ID. The instructions for this are stored in "instruction_codegeneration" above.
####         For that aim we will create a function that allows us to generate the subject_ID while "instruction_codegeneration" is presented.
####         Please insert code at each #.
####         The variable "chars" is a list that will eventually contain all characters that have been pressed. At first, we start by presenting the instructions on
####         the screen (checkpoint1) and then flip the window (checkpoint2). Within a while loop (checkpoint3) we keep updating, drawing and presenting both the instructions (checkpoint4) and the "chars" (checkpoint5) that have been entered. 
####         When the subject is done with entering her code, she will press "Enter" and the function will return the list of characters that have been entered.

def text_writer(msg): 
    chars = []

    visual.TextStim(win, msg, pos=(0, -200)).draw()  ## checkpoint1
    win.flip() ## checkpoint2

    while True: ## checkpoint3
        visual.TextStim(win, msg, pos=(0, -200)).draw() ## checkpoint4
        key = event.waitKeys()[0].lower()
        if key in ("return", "enter"):
            # if we press one of these buttons we would like to break out of the while loop
        elif key == "backspace":
            # if we press "backspace" we would like to delete the last character of chars 
        elif key in "abcdefghijklmnopqrstuvwxyz0123456789":
            # if we press one of these buttons we would like to add it to our list of characters
        else:
            continue
        updated_code = # we have to create a string concatenated from the single characters in the "chars" list; check out the python function "join" (google!).
        # afterwards turn the string to upper case letters using ".upper()"
        visual.TextStim(win, updated_code).draw() ## checkpoint5
        win.flip()
    win.flip()
    return chars





##########################################
#### Generate and assign subject code ####
##########################################
#### TASK 9: Call text_writer() function and pass it the "instruction_codegeneration" as a message. As you know, the text_writer() function, apart from presenting the 
####         code generation screen, also has a return value (i.e., the generated code itself), we can assign this return value to a variable. Assign the function's return value
####         to a variable called "subject_ID".





####################################
#### Present the "proceed_text" ####
####################################
#### TASK 10: Present the "proceed_text" on the screen. Then, wait for the subejct to press "return" or "enter" (argument "keyList"). Finally, create a function called 
####          "proceed_screen()" out of your code, and call the function to present the procede_screen. 






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
    word = # create a TextStim containing the text argument input of the function
    word.draw()
    if phase == "learning": ## for now we are only concentrating on the learning phase
        win.flip()
        core.wait(0.2) ## speeded up a lot for testing purposes (should be 0.5 s)





#####################################################
#### Present a short break before stimulus onset ####
#####################################################
visual.TextStim(win, "").draw() 
win.flip() 
core.wait(2)



######################
#### Close window ####
######################
win.close()



