
from psychopy import visual, core, event
from psychopy import gui
from psychopy import logging

######### TASK 1: CREATE INPUT BOX ###############################################################################
info = {'experimenter':'', 'subject-ID':'', 'gender':['male', 'female', 'diverse'],'version': 1.1, 'feedback': True}
    
infoDlg = gui.DlgFromDict(dictionary=info, title='Setup',
    order=['version', 'experimenter', 'subject-ID', 'gender', 'feedback'], fixed=['version'],
    show=True)
    
######### TASK 2: STOP EXPERIMENT IF CANCEL BUTTON WAS HIT ########################################################  
if not infoDlg.OK:  ## this will be True (user hit OK) or False (cancelled)
    print('User Cancelled') 
    core.quit()


######### TASK 3: SET GLOBAL SHUTDOWN KEY ##########################################################################  
event.globalKeys.clear()
key="q"
def my_func():
    core.quit()
event.globalKeys.add(key=key, func=my_func)

######### TASK 4 - PART 1: CREATE LOGFILE AND PRINT SUBJECT NUMBER ################################################
logfile_name = "logfile_sub{}.csv".format(infoDlg.dictionary["subject-ID"])
with open(logfile_name, 'w') as f:
    print("Subject-ID: "+infoDlg.dictionary["subject-ID"], file=f)


win = visual.Window(size=[500,500], autoLog=True)
rts=[]
keys=[]

texti = visual.TextStim(win, "", name="letter_stimulus", autoLog=True)
stimuli_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
rt_clock = core.Clock()

######### TASK 5: CREATE PSYCHOPY BUILT-IN LOGFILES ################################################
my_log = logging.LogFile(f="logfile_{}.log".format(infoDlg.dictionary["subject-ID"]), level=logging.INFO, filemode="w")

for letter in stimuli_letters:
    texti.setText(letter)
    texti.draw(win)
    
    rt_clock.reset()
    win.flip()
    resp = event.waitKeys(maxWait = 3, timeStamped=rt_clock)
    if resp is not None:
        [(key, rt)] = resp
        keys.append(key)
        rts.append(rt)
        ######### TASK 4 - PART 2: WRITE RESPONSES TO LOGFILE ################################################
        with open(logfile_name, 'a') as f:
            print(key, file=f)
    else:
        keys.append("miss")
        rts.append("miss")
        ######### TASK 4 - PART 3: WRITE MISSES TO LOGFILE ################################################
        with open(logfile_name, 'a') as f:
            print("miss", file=f)

win.close()









