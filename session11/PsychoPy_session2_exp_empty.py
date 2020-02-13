from psychopy import visual, core, event

rts=[]
keys=[]

win = visual.Window(size=[500,500])
rt_clock = core.Clock()
texti = visual.TextStim(win, "")

for letter in ["A", "B", "C", "D", "E", "F", "G"]:

    texti.setText(letter)
    texti.draw(win)

    win.flip()
    rt_clock.reset() # so that RTs are time elapsed since stimulus presentation
    resp = event.waitKeys(maxWait = 3, timeStamped = rt_clock)
    if resp is not None:
        [(key, rt)] = resp
        keys.append(key)
        rts.append(rt)
    else:
        keys.append("miss")
        rts.append("miss")

win.close()
