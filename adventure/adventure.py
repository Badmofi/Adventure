from time import sleep
def goLeft():
    print("You head left and enter a room that is occupied by a sleeping giant. Those who dare to awaken him from his slumber shall surely endure a slow and painful death...")
    print("You now have a choice..do you attempt to bypass him slowly and carefully, or will you try to run past as fast as you can?")
    userInput = ""
    choices = ["1", "2"]
    while userInput not in choices:
        print("Enter '1' for going slowly or '2' for going fast...")
        userInput = input()
        if userInput == "1":
            goSlow()
        elif userInput == "2":
            goFast()
        else:
            print("ERROR: You must enter one of the choices...")
def goSlow():
    print("You make the decision to get past the giant slowly and carefully. Very quietly, you tiptoe past the giant. There are some moments where he stirs and nearly wakes up, but you eventually make it past the giant in one piece!")
    swingingAxes()
def swingingAxes():
    print("You have now entered a room full of gigantic swinging axes that are all lined up in a row in the middle of the room. The route to the next room is on the other side.")
    print("You decide that you have no choice but to attempt to dance your way through, but then you notice some sort of ancient rune written in invisible ink on the wall.")
    print("The rune translates to: 'HIDDEN WITHIN THIS ROOM IS A SECRET PASSAGE THAT LEADS PAST THE AXES. SOLVE THE PUZZLE OF THE COLORED STONES TO REVEAL THE PASSAGE.'")
    print("To your right, you notice a trio of stones colored red, orange, and yellow respectively. You ponder whether or not to solve the puzzle to reveal the secret passage or make an attempt to get past the axes...")
    userInput = ""
    choices = ["1", "2"]
    while userInput not in choices:
        print("If you want to solve the puzzle, enter '1'. If you want to attempt to get past the axes, enter '2'...")
        userInput = input()
        if userInput == "1":
            puzzle()
        elif userInput == "2":
            attempt()
        else:
            print("ERROR: You must enter one of the choices...")
def attempt():
    print("The astonishingly brave soul that you are, you decide to attempt to get through the axes.")
    sleep(5.00)
    print("You manage to get through the axes completely unscathed! The next room will load in two seconds...")
    sleep(2.00)
    crossroads()
def puzzle():
    print("You walk over to the colored stones to attempt to solve the puzzle.")
    print("To reveal the secret passage, you need to select the right stones. Selecting the right stones will get you one step closer to solving the puzzle, while selecting the wrong stones will trigger a booby trap.")
    userInput = ""
    colours = ["red", "orange", "yellow"]
    while userInput not in colours:
        print("Type either 'red', 'orange', or 'yellow' to select that colored stone. HINT: 'The flame shall pass with passion for attention'")
        userInput = input()
        if userInput == "red":
            red()
        elif userInput == "orange":
            orange()
        elif userInput == "yellow":
            yellow()
        else:
            print("ERROR: You must enter one of the choices...")
def red():
    print("You press the red stone. A moment of silence occurs...")
    sleep(5.00)
    print("Then out of nowhere, you are doused in acid from above, causing your skin to deteriorate and you are left as nothing more than a skeleton. Better luck next time!")
    print("THE END")
    quit()
def orange():
    print("You press the orange stone. A moment of silence occurs...")
    sleep(5.00)
    print("then out of nowhere, a part of the wall beside you opens up, and a bunch of arrows begin shooting at you, leaving you as nothing more than a bloody mess. Too bad!")
    print("THE END")
    quit()
def yellow():
    print("You press the yellow stone. A moment of silence occurs...")
    sleep(5.00)
    print("then, the colored stones disband, indicating that you have selected the right stone!")
    print("Now, a trio of gems appear, this time marked by an emerald, a sapphire, and an amethyst.")
    userInput = ""
    colours = ["emerald", "sapphire", "amethyst"]
    while userInput not in colours:
        print("Type either 'emerald', 'sapphire', or 'amethyst' to select that colored stone. HINT: 'Gems of thee are the rarest to be'")
        userInput = input()
        if userInput == "emerald":
            green()
        elif userInput == "sapphire":
            blue()
        elif userInput == "amethyst":
            purple()
        else:
            print("ERROR: You must enter one of the choices...")
def blue():
    print("You select the sapphire. A moment of silence occurs...")
    sleep(5.00)
    print("then out of nowhere, a giant anvil comes soaring down to where you're standing, leaving you nothing more than a bloody, crushed mess. They might've hammered you a little too much. Nice try!")
    print("THE END")
    quit()
def purple():
    print("You select the amethyst. A moment of silence occurs...")
    sleep(5.00)
    print("then out of nowhere, you hear a noise that sounds like air coming out of a pressure cooker. Toxic gas has been released from a hidden canister into the room. You inhale the fumes and inevitably die from it. Sorry...")
    print("THE END")
    quit()
def green():
    print("You select the emerald. A moment of silence occurs...")
    sleep(5.00)
    print("Then, without warning, the floor you're standing on disappears, and you're sent down a long and winding chute, until your feet reach ground...")
    print("You have found the secret passage! Now you can move on to the next room.")
    denOfTemptation()
def denOfTemptation():
    print("You have now come across a room with another ancient rune written in a large size on the tiles of the floor. It reads:")
    print("YOU HAVE ENTERED THE DEN OF TEMPTATION. IN FRONT OF YOU IS A LARGE TREASURE CHEST FILLED WITH SOMETHING TRULY MARVELOUS.")
    sleep(2.00)
    print("IF YOU CHOOSE TO TAKE THE TEMPTATION, WALK OVER AND OPEN THE CHEST. IF YOU DECIDE NOT TO, PRESS THE RED BUTTON NEXT TO THE CHEST AND A DOOR WILL OPEN TO THE NEXT ROOM.")
    sleep(2.00)
    print("Well..? You heard the rune. Choose!")
    sleep(1.00)
    userInput = ""
    choices = ["7", "8"]
    while userInput not in choices:
        print("If you want to open the treasure chest, type '7'. If not, type '8'...")
        userInput = input()
        if userInput == "7":
            openChest()
        elif userInput == "8":
            leaveRoom()
        else:
            print("ERROR: You must enter one of the choices...")
def leaveRoom():
    print("As much as you would like to see what is inside the treasure chest, you fear something terrible might happen if you open it, so you push the red button to open the door, and enter the hallway leading to the next room...")
    sleep(2.00)
    crossroads()
def crossroads():
    print("You wander down a long, winding hallway, when suddenly you find that the hallway now splits into two paths, one going left, one going right.")
    print("There is a sign that says 'LEFT: GIANT FALSE-WIDOW SPIDER WEB; RIGHT: THICKET OF VINES, PRICKERS AND THORNS'")
    print("Choose which direction you want to head in...")
    userInput = ""
    choices = ["1", "2"]
    while userInput not in choices:
        print("If you want to face the giant spider, type '1'. If you want to brave the vines, type '2'...")
        userInput = input()
        if userInput == "1":
            spider()
        elif userInput == "2":
            vines()
        else:
            print("ERROR: You must enter one of the choices...")
def spider():
    print("You decide to brave the giant spider and you head left.")
    sleep(1.00)
    print("You have now entered a huge chamber covered in gigantic cobwebs. You look up at the ceiling and see a gigantic black shape sort of hovering in mid-air. You take a few steps forward to get a closer look, when suddenly, the shape starts falling to the ground!")
    print("You jump backwards out of the way, and gaze up at the great beast that has just dropped down in front of you. It's a gigantic false-widow spider! Before you can say another word, the spider shoots out a poisonous web in your direction, glueing you to where you are standing...")
    print("The spider starts advancing on you, a menacing glare in its eyes, and you have no choice but to try to move out of the way...")
    userInput = ""
    choices = ["left", "right", "forwards", "backwards"]
    while userInput not in choices:
        print("Type 'left', 'right', 'forwards' or 'backwards' to move in that direction...")
        userInput = input()
        if userInput == "left":
            print("You dart to the left to dodge the spider, but it swiftly changes course and before you know it, the spider has reached you and is eating you alive.")
            print("THE END")
            quit()
        elif userInput == "forward":
            print("Hey, stupid! You just got CLOSER to the spider! The spider swiftly reaches you and eats you alive. Enjoy the afterlife...")
            print("THE END")
            quit()
        elif userInput == "backwards":
            print("You start jumping backwards as fast as you can, but you soon find yourself backing into a wall. The spider quickly catches up with you and eats you alive...")
            print("THE END")
            quit()
        elif userInput == "right":
            print("You hop to the right, JUST before the spider reaches you. It's too late for the spider to change course, and it crashes head-first into the brick wall.")
            print("The spider stirs for a moment...")
            sleep(3.00)
            print("All of a sudden, it gets back on its feet and turns to face you once again. It's not over yet...")
            spiderPart2()
        else:
            print("ERROR: You must enter one of the choices...")
def spiderPart2():
    userInput = ""
    choices = ["left", "right", "forwards", "backwards"]
    while userInput not in choices:
        print("Type 'left', 'right', 'forwards' or 'backwards' to move in that direction...")
        userInput = input()
        if userInput == "left":
            print("You start to hop to the left, but eventually, you have found that you have backed straight into a corner!")
            print("Within seconds, the spider catches up with you and crushes your head into pieces...")
            print("THE END")
            quit()
        elif userInput == "forward":
            print("Hey, stupid! You just got CLOSER to the spider! The spider swiftly reaches you and eats you alive. Enjoy the afterlife...")
            print("THE END")
            quit()
        elif userInput == "right":
            print("You start jumping to the right as fast as you can. You seem to be getting away from it, until you find yourself catching onto one of the webs and sticking yourself to the wall.")
            print("The spider catches up with you and crushes your head into many fleshy, bloody pieces...")
            print("THE END")
            quit()
        elif userInput == "backwards":
            print("You start hopping backwards as fast as humanly possible, then you stop hopping and wait for the spider to get closer.")
            print("Then, at the last minute, you leap out of the way to let the spider once again smash straight into the brick wall...")
            print("For a moment, you think you have actually defeated it...")
            sleep(2.00)
            print("All of a sudden, it gets back on its feet and turns to face you once again. It uses on of its eight long legs to hit a hidden floor switch on the floor.")
            print("You hear a loud rumbling noise coming from behind you. You turn around and find that the floor behind you has just disappeared, being replaced by a seemingly bottomless pit...")
            print("Your next move is the most crucial of all. With going backwards being out of the question now, you must choose wisely...")
            spiderPart3()
        else:
            print("ERROR: You must enter one of the choices...")
def spiderPart3():
    userInput = ""
    choices = ["left", "right", "forwards"]
    while userInput not in choices:
        print("Type 'left', 'right', or 'forwards' to move in that direction...")
        userInput = input()
        if userInput == "right":
            print("You take a huge hop to the right, but your feet land on something...funny..")
            print("You bend down and clear away the webs to discover that you have just landed on a big red floor switch! Once again, you hear a loud rumbling sound, and before you know it, the entire floor collapses beneath your feet, and both you and the spider start falling to your inevitable demises...")
            print("THE END")
            quit()
        elif userInput == "forward":
            print("Hey, stupid! You just got CLOSER to the spider! The spider swiftly reaches you and eats you alive. Enjoy the afterlife...")
            print("THE END")
            quit()
        elif userInput == "left":
            print("You jump to the left, but your feet land on something...funny..")
            print("You bend down and clear away the webs to discover that you have just landed on a big red floor switch! Once again, you hear a loud rumbling sound...")
            sleep(2.00)
            print("Then, the part of the floor the spider is standing on collapses, and the spider falls through the hole and disappears completely!")
            print("Still reeling from the ordeal with the spider, you take a moment to catch your breath, then a door opens on the opposite wall. You head through it...")
            sleep(3.00)
            exit()
        else:
            print("ERROR: You must enter one of the choices...")
def vines():
    print("You decide to face the vines and head right.")
    sleep(1.00)
    print("You have now entered a room filled wall-to-wall with thick, overgrown vines, all lined with prickers and thorns.")
    print("It seems like the only way to the other side is to painfully tangle your way through the vines...but then your eyes see a narrow opening at the bottom of the thicket, completely free of prickers and thorns, but a claustrophobe's worst nightmare.")
    print("You cringe at the uncomfortable nature of this choice as you are a claustrophobe yourself, but it's now up to you to decide whether to endure a claustrophobic, but painless crawl UNDER the vines, or a painful but quick run straight THROUGH the vines... ")
    userInput = ""
    choices = ["over", "under"]
    while userInput not in choices:
        print("Type 'over' or 'under' to indicate how you want to get through the vines...")
        userInput = input()
        if userInput == "over":
            over()
        elif userInput == "under":
            under()
        else:
            print("ERROR: You must enter one of the choices...")
def under():
    print("You decide to face your fear of tight spaces and crawl under the thorns.")
    print("Getting on the floor, you take a deep breath and start to shimmy your way through. You keep your eyes shut the entire time, trying not to think about the tight space surrounding you..")
    sleep(3.00)
    print("At last, you make it to the other side, completely thorn free and more importantly, taking a huge step of overcoming your claustrophobia. Excellent work!")
    sleep(2.00)
    lasers()
def lasers():
    print("If you thought the vine room was bad, here comes a whole other level of insane...")
    print("This next room presents you with a web of LASERS! One wrong move trying to get through this and you're as good as gone..")
    sleep(1.00)
    print("Then your attention shifts to a trio of stone wheels containing numbers from 1 to 9 on the wall to your left. An ancient inscription is written below:")
    print("TO DISABLE THE LASERS FOR FIVE SECONDS, YOU MUST ENTER THE CORRECT NUMBER COMBINATION ON THE WHEELS.")
    print("You decide to solve the puzzle to disable the lasers, because there is no WAY you are surviving them. Then you examine further and see that there appears to be a hint beneath the inscription...")
    print("104 _ 3 _ 116")
    print("It looks like some of the hint has rotted away over time...it looks to be some sort of equation that provides a hint to the correct combination, but you aren't sure which operands go where...")
    userInput = ""
    answer = "428"
    print("Enter three numbers to solve the puzzle. (EXAMPLE INPUT: 123) ")
    userInput = input()
    if userInput == answer:
        correct()
    else:
        incorrect()
def correct():
    print("You have entered a three-digit combination. A moment of silence occurs...")
    sleep(5.00)
    print("Suddenly, you see that the lasers disappear. The combination worked! You make a mad dash through the room before the five seconds runs out. Then there's trouble...")
    sleep(2.00)
    print("You trip on a loose stone and end up losing your shoe! Knowing that the clock is ticking, you struggle to decide whether to go on without the shoe or go back and grab it.")
    userInput = ""
    choices = ["5", "6"]
    while userInput not in choices:
        print("Hurry up and choose!! Enter 5 to grab the shoe or 6 to go on without it...")
        userInput = input()
        if userInput == "5":
            getShoe()
        elif userInput == "6":
            leaveShoe()
        else:
            print("ERROR: You must enter one of the choices...")
def leaveShoe():
    print("You decide it's not worth risking your life for a shoe and decide to go on without it. You make it past the lasers just in time for them to reactivate.")
    print("Around the corner, you see some sort of bright light. You wander towards it...")
    sleep(2.00)
    exit()
def getShoe():
    print("In the heat of the moment, you dive backwards and snatch the shoe back. But less than a second later, the five-second timer runs out, and the lasers reactivate and slice your body into pieces. Better luck next time...")
    print("THE END")
    quit()
def incorrect():
    print("You have entered a three-digit combination. A moment of silence occurs...")
    sleep(5.00)
    print("Suddenly, another ancient inscription appears underneath the old one:")
    print("Puzzle...failed. You have entered the incorrect combination.")
    sleep(2.00)
    print("Before you get a second to think, a light shines on you from above and without warning, a giant laser shoots at you, killing you on the spot. Better luck next time...")
    print("THE END")
    quit()
def over():
    print("You decide NOT to endure the crawl and decide to go right through the vines.")
    sleep(1.00)
    print("Closing your eyes and pausing for a second, you leap straight into the thicket and starting thrashing about, getting pricked by the thorns all the while, when suddenly, there's trouble...")
    sleep(2.00)
    print("You feel the vines starting to move...they're still growing, and they're surrounding you! You attempt to keep trekking through, but the vines keep surrounding you, until some of them start wrapping around you like a boa constrictor and squeezing you tightly.")
    sleep(1.00)
    print("You gasp for air but eventually, you officially run out of breath and succumb to the wrath of the vines...")
    print("THE END")
    quit()
def openChest():
    print("Your curiosity gets the better of you and you decide to open the treasure chest")
    print("You open the chest, and find that it is filled to bursting with delicious treats of all kinds...donuts with powdered sugar and jelly filling, cupcakes with pink icing and sprinkles, and green tea infused coconut macaroons...")
    print("Your stomach rumbles from seeing all the food, and after all, you hadn't eaten in 500 years, so you immediately start tucking in...")
    print("Eventually, you have eaten all of the goodies in the chest, and are left as a fat lazy lump. As you ready yourself for a well deserved nap, you feel the floor start to crumble beneath you...")
    print("The floor gives way, and you fall for what seems like an eternity, until finally, you are caught by a series of chains confining your legs to a treadmill. The treadmill starts up automatically, and, being bound to the treadmill, you have no excuse but to accept that 'Leg Day' is a thing, and start running to burn off all those calories.")
    print("There is nothing you can do except just let it happen, but hey, a little exercise certainly wouldn't hurt you. Better luck next time, tubby!")
    print("THE END")
    quit()
def goFast():
    print("You think it over and decide to try to get past the giant as fast as you possibly can.")
    print("You start to make a mad dash past the giant to the door on the other side of the room, but then there's trouble...")
    print("Your footsteps reverberate around the room, and the sleeping giant wakes up! Predictably infuriated at having been woken up, the giant clomps in your direction, but you're far too busy pissing yourself to run away...")
    print("The giant picks you up with his big hand, and then suddenly, the last thing you hear is an ear-splitting CRACK! The giant has crushed your bones and you are now nothing but a spineless (literally) mess. Maybe it would have been a wiser choice to go SLOWLY around the giant...")
    print("THE END")
    quit()
def goRight():
    print("You head right and find that an elderly lady in a black robe is blocking the entrence to the next room.")
    print("'You are the chosen one', she says ominously. 'Wear this ring...it will determine your fortune...your destiny...'. She now holds a creepy-looking ring up to you.")
    print("You think this old hag is off her medication, and are about to shove her out of your way...but at the same time, you are quite curious as to what she meant by 'fortune and destiny'...")
    print("It's now up to you to decide whether you accept the ring, or refuse it...")
    userInput = ""
    choices = ["a", "b"]
    while userInput not in choices:
        print("Enter 'a' to accept the ring or 'b' to refuse the ring...")
        userInput = input()
        if userInput == "a":
            acceptRing()
        elif userInput == "b":
            refuseRing()
        else:
            print("ERROR: You must enter one of the choices...")
def acceptRing():
    print("Your curiosity compells you to accept the ring from the old woman...but then there's trouble...")
    print("As you put the ring onto your finger, a dark, black mist starts to fill the room. Then, you hear really loud cackling coming from the old woman.")
    print("Eventually, the mist overwhelms you, and you gradually start to lose your sense of hearing and sight, until finally, everything comes to a stop. Now permanently stuck in an endless, dark void, you start to regret your decision to take the ring...")
    print("THE END")
    quit()
def refuseRing():
    print("You decide to refuse the ring from the old woman, but before you can advance, the woman slowly but surely starts to grow larger in stature...")
    print("Eventually, she grows to be nearly the size of the entire room! Eyeing you with a furious gaze, she wiggles her fingers and sends lightning flashes in your direction.")
    print("You try your best to dodge them but eventually, one ends up hitting you! In your very last moments of life, you deeply regret not accepting that ring...")
    print("THE END")
    quit()
def exit():
    print("CONGRATULATIONS!!! You have found an exit. Freedom is yours!")
    quit()
if __name__ == "__main__":
    print("PYTHON ADVENTURE GAME")
    print("Written and Programmed by Carter Barton")
    print("Additional Material/Ideas by Richard Clark")
    sleep(6.00)
    print("You are awoken from a 500-year slumber by the sound of pounding rain...")
    print("You see that you are standing in a pool of water in the middle some sort of shrine, but you have no recollection of how you got there...")
    print("It is now up to you to navigate your way out of this shrine and get back to the real world")
    print("Enter your name to get started: ")
    name = input()
    print(name + ", it is time to begin your quest")
    print("First, you have the choice of heading either left or right")
    userInput = ""
    choices = ["left", "right"]
    while userInput not in choices:
        print("Enter 'left' or 'right' on your keyboard...")
        userInput = input()
        if userInput == "left":
            goLeft()
        elif userInput == "right":
            goRight()
        else:
            print("ERROR: You must enter one of the choices...")

