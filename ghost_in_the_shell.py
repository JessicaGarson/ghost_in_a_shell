print "Welcome to Ghost in the Shell! This is a text based game."
print """It's the year 2029, you just woke up feeling confused and you can no longer feel your limbs in the way you used to. You are floating in a fishbowl. You have 2 options. \n \nOption A - Fight the lady awkwardly hovering over you. \nOption B - Talk to the woman and learn your origin story."""

selection = raw_input("Please select the letter of the option you select: ")
selection = selection.upper()

fighting_story = ["You have chosen to fight. You amaze yourself with just how good you are at fighting. You realize that you have no memories anymore you are stuck in a fog. You wonder the brightly colored streets until the cops come for you and take you away.", """\nYou have two options. \n \nOption A - Use your new super human strength to break open your handcuffs and continue your life on the run. \nOption B - Save your super hero skills for later so that you might be able to get some answers and cause damage to the real bad guys at a later point.""", "You meet a man from your past, who knew you when you were fully human. The company attempted to do the same for him but they were less successful. You join forces and use your skills to fight your makers."]
hq_story = ["You get told that your name is Major, and a backstory that doesn't seem to fit with what you think you know about yourself. This situation seems fishy. You get told that you are the first of your kind since you have synthetic body and a human brain.", """\nYou have two options. \n \nOption A- You can battle your makers and search on your own for answers. \nOption B - you continue on and join an elite unit called Section 9 of humans with advanced cyborgnetic enhansements. You can continue continue on and fight who you are told to.""", "You are assigned to fight a man. It turns out you know this person from your past. He tells you, he knew you when you were fully human. The company attempted to do the same for him but they were less successful. You join forces and use your skills to fight your makers.", "You meet a man from your past, who knew you when you were fully human. The company attempted to do the same for him but they were less successful. You join forces and use your skills to fight your makers."]

def second_storyline(selection, fighting_story, hq_story):
    fighting_selection = ""
    hq_selection = ""
    if selection == "A":
        print fighting_story[0]
        print fighting_story[1]
        fighting_selection = raw_input("Please select the number of the option you select: ")
        fighting_selection = fighting_selection.upper()
    elif selection == "B":
        print hq_story[0]
        print hq_story[1]
        hq_selection = raw_input("Please select the number of the option you select: ")
        hq_selection = hq_selection.upper()
    return fighting_selection, hq_selection

fighting_selection, hq_selection = second_storyline(selection=selection, fighting_story=fighting_story, hq_story=hq_story)

def third_storyline_fighting(fighting_selection, fighting_story, hq_story):
    hq_selection = ""
    if fighting_selection == "A":
        print fighting_story[2]
    elif fighting_selection == "B":
        print hq_story[0]
        print hq_story[1]
        hq_selection = raw_input("Please select the number of the option you select: ")
        hq_selection = hq_selection.upper()
    return hq_selection

hq_selection = third_storyline_fighting(fighting_selection=fighting_selection, fighting_story=fighting_story, hq_story=hq_story)


def end_it(hq_story, hq_selection):
    if hq_selection == "A":
        print hq_story[2]
    elif hq_selection == "B":
        print hq_story[3]
end_it(hq_story=hq_story, hq_selection=hq_selection)
print "Thanks for playing!"
