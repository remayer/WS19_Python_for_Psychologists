#!/usr/bin/python
#-- coding: UTF-8 --
##### Experiment adapted from: 
## Nehler, K. J. & Sassenhagen, J. (2020). DRM-Paradigm with Psychopy: An in-depth look at Programming Experiments. In S.E.P. Boettcher, D. Draschkow, J. Sassenhagen & M. Schultze (Eds.). *Scientific Methods for Open Behavioral, Social and Cognitive Sciences*. https://doi.org/10.17605/OSF.IO/M2YDS

from __future__ import unicode_literals, print_function, division  
from random import shuffle
from random import choice
from psychopy import visual, event, core, monitors 

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
             "7sleep": ["bed", "rest", "awake", "tired", "dream", "wake", "snooze", "blanket", "doze", "slumber"]} 

old_future = "process automation specialist,e-commerce manager,solutions designer,data analyst,developer".split(",")
old_past = "assembly-line worker,carpenter,shoemaker,smith,glassblower".split(",")
new_future = "user experience designer,machine learning specialist,risk manager,scientist,management consultant".split(",")
new_past = "accountant,secretary,mailman,craftsman,construction draftsman".split(",")

recognition_items = "accountant,aunt,bike,calm,chilly,coal,construction draftsman,craftsman,fish,kiwi,legs,machine learning specialist,mailman,management consultant,muscle,piano,plane,radio,ripe,risk manager,royal,scientist,secretary,sliding window,snooze,sock,syringe,tired,ugly,user experience designer,valley,wine,winter,wood".split(",")


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

goodbye_text = "Thank you for your participation. Press ENTER to exit the experiment."


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
    return new_code



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
    show_words(text=stim, phase="learning")





##################################
#### Present the proceed text ####
##################################
#### TASK 12: Present the proceed_screen()
proceed_screen()





########################################
#### Create the recognition stimuli ####
########################################
#### TASK 13: Now, we need to create a list of words that will be presented during the recognition phase. So far, the list "recognition_items" only contains words
####          from neutral words that are irrelevant "distractors" as well as new target words from both the "future" and the "past" category that will be presented 
####          to our subject independent of her/his condition. However, we have to add old items from each subject's learning phase. These have already been
####          pre-selected in the lists "old_future" and "old_past". Depending on the subject's condition, add these words to the "recognition_items".
if condition == "past":
    recognition_items.extend(old_past)
elif condition == "future":
    recognition_items.extend(old_future)



#########################################
#### Shuffle the recognition stimuli ####
#########################################
#### TASK 14: Shuffle the recognition_items.
shuffle(recognition_items)




############################################################
#### Create a legend presented during recognition phase ####
############################################################
#### TASK 15: During the presentation of the recognition items subjects should see a legend showing them which key represents which answer. 
####          The key assignment (whether "A" stands for "learned" or for "new"), however, should be random. That is, you will need to randomly assign
####          the two keys "A" and "L" to the two answers "Learned" and "New". 
answer_keys = ["A", "L"]
shuffle(answer_keys)
key_assign = dict(zip(answer_keys, ["Learned", "New"]))
legend = visual.TextStim(win, "A ({})                                            L ({})".format(key_assign["A"], key_assign["L"]), pos=(25, -200))





#########################################################
#### Extend show_word function for recognition phase ####
#########################################################
#### TASK 16: Return to the function you created in TASK 11. Change it, so that you can use it during the recognition phase as well to present the recognition_items.
####          During the recognition phase, each item should be presented as well as the legend. until subjects give a response. As the response should be logged 
####          we will need to reset the clocki before. Use the function "win.callOnFlip()" to reset the clock at the same time as the window flip occurs. 
####          After the stimulus + legend have been presented wait for the subject's response (both RT and key pressed). Only the keys "a" and "l" should be usable during the response window.
####          Moreover, we would like to save the response to a logfile. First, we need a file_name. Create the file_name before the function definition as a ".csv" file that also contains 
####          each subject's name, their condition (future or past) and the key that represented the answer "Learned". We have already printed the header line to the file for you.
####          Afterwards, you will have to return to your function definition to write the word presented during the trial, its wordtype (see below), the key pressed and the reaction time to the logfile.
####          The wordtype is supposed to be "neutral" in case the word was from one of the non-profession categories. In case the word was a learned word from the subject's profession category
####          "old_future" or "old_past" (depending on condition) should be logged. If the word comes from the new_future list, "new_future" whould be logged. If the word comes from the new_past list
####          "new_past" should be logged. In any other case "neutral" should be logged.
####          By the way, normally, we wouldn't define the same function twice inside one script, but would rather define it once, maybe somewhere in the upper part of the script.
####          But for purposes of easier separation of the process into single tasks, we will just define the function again, down here.

file_name = subject_ID + "_"+ condition + "_Learned"+ answer_keys[0]+ ".csv"
with open(file_name, "w") as f:
    print("word,wordcategory,key,rt", file=f)

def show_words(text, phase):
    word = visual.TextStim(win, text)
    word.draw()
    if phase == "learning": # for now we are only concentrating on the learning phase
        win.flip()
        core.wait(0.2) # speeded up a lot for testing purposes (should be 0.5 s)
    elif phase == "recognition":
        legend.draw()
        win.callOnFlip(clocki.reset)
        win.flip()
        key, rt = event.waitKeys(timeStamped=clocki, keyList =("a","l"))[0] 
        word_category = "old_future" if text in old_future else ("old_past" if text in old_past else ("new_future" if text in new_future else ("new_past" if text in new_past else "neutral")))
        with open(file_name, "a") as f:
            print("{},{},{},{}".format(text,word_category,key_assign[key.upper()],rt), file=f)
        



###################################
#### Present recognition words ####
###################################
#### TASK 17: Present the recognition_items in a loop using your show_words() function.
for word in recognition_items:
    show_words(word, phase="recognition")




########################
#### Goodbye-Screen ####
########################
#### TASK 18: Present the goodbye_text from above. Wait for the subject to press "enter" or "return".
visual.TextStim(win, goodbye_text).draw() 
win.flip() 
event.waitKeys(keyList = ["return", "enter"]) 





######################
#### Close window ####
######################
win.close()








