import colorama
import time
import os
import time
import sys
def animate_text_everything(text, delay=0.05):
    for char in text:
        sys.stdout.write(colorama.Fore.LIGHTBLACK_EX + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def animate_text_everything_empasis(text, delay=0.5):
    for char in text:
        sys.stdout.write(colorama.Fore.LIGHTBLACK_EX + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def animate_text_shaman(text, delay=0.05):
    for char in text:
        sys.stdout.write(colorama.Fore.LIGHTGREEN_EX + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def non_main_speak(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def minako_speak(text, delay=0.05):
    for char in text:
        sys.stdout.write(colorama.Fore.LIGHTMAGENTA_EX + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def minako_speak_you(text, delay=0.05):
    for char in text:
        sys.stdout.write(colorama.Fore.MAGENTA + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def screen_clear():
    os.system('cls')
def first_room1( ):
    door_lock_room_1 = True
    puzzle_loop = True
    screen_clear()
    animate_text_everything('minako awakens al0ne in a ro0m that is n0t their own in a bed that is n0t theirs')
    minako_speak('w-where am I. i-is anyone there?')
    while puzzle_loop == True:
        interact = input(animate_text_everything('in the room there is a 0ld computer, a window with m00nlight spilling th0ugh, a 0ld remote on a bedside table and a door what do you want t0 interact with.'))
        if interact == "computer" or interact == "old computer":
            old_computer_password = int(input(animate_text_everything('the c0mputer requires a 4 digit number passw0rd try and input one')))
            if old_computer_password == 6308:
                animate_text_everything('hello player i d0nt know why you are trying to save this dying w0rld but if you are g0ing to try then remember')
                screen_clear()
                animate_text_everything_empasis('you only have one chance')
                screen_clear
                door_lock_room_1 = False
                
        if interact == "remote" or interact == "old remote":
            animate_text_everything('minako walks up to the remote and picks it up all the butt0ns are faded exept for 4 butt0ns on the number pad')
            animate_text_everything('minako picks up the remote')
            remote = True
            minako_speak('its too dark to read what the buttons say')
            screen_clear
        if interact == "window":
            animate_text_everything_empasis('dim m00nlight faintly trikles out the window iluminating the area around it')
            if remote == True:
                animate_text_everything('the dim light iluminates the buttons on the remote')
                minako_speak('i can use the light to read the buttons')
                minako_speak('huh all the buttons are scratched off exept 6, 3, 0, and 8')
                time.sleep(1)
                screen_clear
        if interact == "door":
            animate_text_everything('minako walks up to the door and tries to open it')
            if door_lock_room_1 == True:
                minako_speak('sigh the door is locked')
            else:
                animate_text_everything('minako places their hand on the handle and opens the door entering the next room')
                minako_speak('the door is unlocked')
                puzzle_loop = False
def second_room2():
    screen_clear()
    animate_text_everything('as minako enters the the d00r shuts beheind them and locks with a loud click')
    animate_text_everything('the room is dark very dark the 0nly light at all in it is a faint glimmer of s0me kind of glass object acr0ss the room')
    time.sleep(1)
    screen_clear()
    minako_speak('its so dark in here i cant see anything')
    minako_speak('wait whats that')
    time.sleep(1)
    screen_clear()
    animate_text_everything('minako apr0aches the small glass object, their luminous yellow eyes reflecting on its surface')
    animate_text_everything('as minako places their hands of it the area is iluminated by a glow from the orb')
    time.sleep(1)
    screen_clear()
    minako_speak('a snowglobe?')
    animate_text_everything('in minakos hands rests an incredibly large snowglobe about the size of a basketball thats gives of a faint glow')
    animate_text_everything('in the snowglobe is a highly detailed map of the world seemingly divided into 3 areas with a large tower in the center')
    animate_text_everything('the outermost area is a baren wasteland with seemingly no life to be found')
    animate_text_everything('the middle area is a form of marshland with many small villages scattered around')
    animate_text_everything('the inner area is a cityscape with some form of green liquid in the place of lakes')
    animate_text_everything('and in the very center is a tower that extends all the way out to the very top of the globe looming over everything else')
    time.sleep(1)
    screen_clear()
    animate_text_everything('the faint glow coming off the snowglobe speads a faint light around the room this faint light is just enough for ninako to be able to make out the shape of a door across the room')
    minako_speak('that must be the way out')
    animate_text_everything('as minako opens the door bright light spills into the room from the outside')
    animate_text_everything('as minakos eyes adjust to the glaring light the outside clarifys in their vision')
    animate_text_everything('minako sees a vast expanse of wasteland seemingly devoid of anything except for a few structures spaning out to where the horizen should be')
    screen_clear
def wastes_1():
    animate_text_everything('minako aproaches the nearest structure a old shack and knocks on the door')
    minako_speak('hello is anyone home?')
    animate_text_shaman('ahh a visitor')
    animate_text_everything('the sound of footsteps resound from the building as the door creaks open revealing a strangly dressed elderly man or women their much to old to be able to tell')
    animate_text_shaman('finaly the messaiah has arived as fortold')
    screen_clear()
    minako_speak('who are you?')
    animate_text_shaman('i am the shaman the one who waits to guide the messaiah')
    minako_speak('who is this messiah')
    animate_text_shaman('why you are of course, the fact you hold the new horizen proves it')
    minako_speak('but im not holding any horizen all i have is this snowglobe')
    animate_text_shaman('but that "snowglobe" you hold is the new horizen')
    minako_speak('what do you mean and what is this prophecy')
    animate_text_shaman('i suppose i should tell you the prophecy')
    screen_clear()
    animate_text_shaman('it began many years ago when the old horizen shattered and the border that defined the differented the land and the sky blurred as they became one')
    animate_text_shaman('at that time the shaman before me was given a prophecy')
    animate_text_shaman('the prophecy fortold that a child of another world would emerge with the ability to speak to god themself, a messiah')
    animate_text_shaman('guided by the word of god that child would bring the new horizen to the top of the world and restore the border between land and sky')
    animate_text_shaman('almost half the world has already been consumed')
    animate_text_shaman('and the messiah destined to stop this is you')
    animate_text_shaman('and the god meant to guide them is')
    screen_clear()
    time.sleep(0.5)
    animate_text_everything_empasis('You')
    time.sleep(1)
    screen_clear()
    minako_speak('im supposed to be able to speak to god but i havent heard anything from them')
    animate_text_shaman('that is strange')
    animate_text_shaman('you should be able to speak to them by thinking with the intent for them hear')
    animate_text_shaman('give it a try')
    minako_speak('ok ill try')
    screen_clear()
    first_talk = input(f"{minako_speak_you('hello god? are you there?')} yes or no")
    if first_talk == "yes":
        minako_speak_you('so you are real!')
        name = input(minako_speak_you('hi im minako whats your name'))
wastes_1()
print(__name__)











