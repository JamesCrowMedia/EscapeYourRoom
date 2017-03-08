import time
import sys

#These variables control the delays
dChoice = 5
dEnd = 10

#These are for formatting and animation
def wipe(n=4, line=True):
    print("\n"*n)
    if line == True:
        print('-'*20)

def delay(n=3):
    for i in range(n):
        time.sleep(.75)
        print('.', end=" ")
        sys.stdout.flush()
    print('\n')

def drama():
    for i in range(2):
        print("DUN ", end='')
        sys.stdout.flush()
        time.sleep(.75)
    print("D", end='')
    for i in range(30):
        print('U', end='')
        sys.stdout.flush()
        time.sleep(.05)
    print("N", end='')
    for i in range(15):
        print('!', end='')
        sys.stdout.flush()
        time.sleep(.05)

def gameOver(win=False):
    time.sleep(1)
    delay(dEnd)
    if win == False:
        drama()
        for c in "\n\nYou lost!...\nPlease try again, or whatever...\n\n":
            time.sleep(.1)
            print(c, end="")
            sys.stdout.flush()
    else:
        for c in "VICTORY!... But, now you are locked in the house. :(\n\n":
            time.sleep(.1)
            print(c, end="")
            sys.stdout.flush()
    for c in "\n\nGame by Kasey and James\n":
        time.sleep(.1)
        print(c, end="")
        sys.stdout.flush()
    print("\nPlay again?")
    delay(dChoice)
    choiceList = ['yes', 'no']
    choice = action(choiceList)
    if choice == 'yes':
        user.userReset()
        main()
    else:
        print("Thank you for leaving.")
        sys.exit()


#These are helper functions
def sceneOpen(string):
    wipe()
    print(string)
    delay()

def action(choiceList):
    choice = ''
    i = 0
    valid = False
    while valid == False:
        choice = input("What do you choose? type " + str(choiceList) + "  ")
        if choice in choiceList or i > 10:
            valid = True
        i += 1
    if i >= 9 or choice == '':
        print("You are too bad at typing to play this game.")
        sys.exit()
    return choice

def checkState():
    if user.getClothes() > 15:
        print("You are wearing WAAAAY to many clothes.")
        delay()
        print("You fell over, and can no longer stand up.")
        gameOver()

def openJournal():
    sceneOpen('''You see a code, "The crow flies at midnight."''')
    print('''"Lockbox: 314" is also written in there.''')
    user.addInv("code")
    delay(dChoice)
    user.dropInv("journal key")

def openBox():
    sceneOpen("You input combination...")
    time.sleep(.5)
    for c in "\n\n3...1...4...\n\n":
        time.sleep(.25)
        print(c, end="")
        sys.stdout.flush()
    delay(dChoice)
    print("It's empty. Maybe you should have shook it instead of wasting all that time.")
    delay(dChoice)
    user.dropInv("code")

#Player Class --------------------
class Player():
    def __init__(self):
        self.inv = {"journal key": False, "journal": False, "screwdriver": False, "lockbox": False, "code": False, "door key": False}
        self.pants = 1
        self.shirts = 1
    def userReset(self):
        self.inv = {"journal key": False, "journal": False, "screwdriver": False, "lockbox": False, "code": False, "door key": False}
        self.pants = 1
        self.shirts = 1

    def invCheck(self, item):
        return self.inv[item]

    def getInv(self):
        invEmpty = True
        print("You are carrying:")
        for item in self.inv:
            if self.inv[item]:
                print(item)
                invEmpty = False
        if invEmpty:
            print("nothing")
    def morePants(self):
        self.pants += 1
        if self.pants > 10:
            return "You can no longer move your legs. You now waddle."
        elif self.pants > 5:
            return "This is getting weird."
        else:
            return "You are now wearing " + str(self.pants) + " pairs of pants."

    def moreShirts(self):
        self.shirts += 1
        if self.shirts > 10:
            return "You now have the arm articulation of a T-Rex wearing " + str(self.shirts) + " shirts."
        elif self.shirts > 5:
            return "You are the master of unnecessary layering."
        else:
            return "You are now wearing " + str(self.shirts) + " shirts."

    def getClothes(self):
        return self.shirts + self.pants

    def addInv(self, item):
        self.inv[item] = True

    def dropInv(self, item):
        self.inv[item] = None

#Home Scene --------------------
class Home:
    def __init__(self):
        self.i = 0
        self.opening = {0:"You look around.", 1:"You look around. You've done that before!", 2:"You look at the room. Again.", 3:"You look around. Everything looks the same!"}
    def goHome(self):
        checkState()
        sceneOpen("You are in the center of the room.")
        print(self.opening[self.i])
        self.i = self.i%3 + 1
        delay()
        print("Here are your options:")
        choiceFullText = "Look by the bed | Look in the dresser | Look at the desk | Look at the window | Check out the door"
        choiceList = ['bed', 'dresser', 'desk', 'window', 'door', 'inventory']
        if user.invCheck("journal key") == True and user.invCheck("journal") == True:
            choiceFullText += " | Open the journal"
            choiceList += ["open journal"]
        if user.invCheck("code") == True and user.invCheck("lockbox") == True:
            choiceFullText += " | Open the lock box"
            choiceList += ["open box"]
        print(choiceFullText)
        delay(dChoice)
        choice = action(choiceList)
        if choice == 'bed':
            b1.goBed()
        elif choice == 'dresser':
            d1.goDresser()
        elif choice == 'desk':
            dsk.goDesk()
        elif choice == 'window':
            w1.goWindow()
        elif choice == 'door':
            door.goDoor()
        elif choice == 'inventory':
            user.getInv()
            delay(dChoice)
            self.goHome()
        elif choice == 'open journal':
            openJournal()
            self.goHome()
        elif choice == 'open box':
            openBox()
            self.goHome()
        else:
            print("You broke it!")
            self.goHome()

#Bed Scene --------------------
class Bed:
    def __init__(self):
        self.i = 0
        self.opening = {0:"You see your halfheartedly made bed.", 1:"Your unmade bed invokes a feeling a parental disappointment.", 2:"Someday, bed. Someday."}
    def goBed(self):
        sceneOpen(self.opening[self.i])
        self.i = (self.i + 1) % 3
        print("Here are your options:")
        print("Look under the bed | Look under the pillow | Look on the night stand")
        delay(dChoice)
        choiceList = ['underbed', 'pillow', 'stand', 'back up']
        choice = action(choiceList)
        if choice == 'underbed':
            self.goUnderbed()
        elif choice == 'pillow':
            self.goPillow()
        elif choice == 'stand':
            self.goStand()
        elif choice == 'back up':
            h1.goHome()
        else:
            print("You broke it!")
            self.goBed()

    def goUnderbed(self):
        sceneOpen("You see a monster-shaped indent in the carpet.")
        self.goBed()

    def goPillow(self):
        if user.invCheck("journal key") == False:
            sceneOpen("You see a key and the bottom of your stupid pillow.")
            print("Here are your options:")
            print("Take the key")
            delay(dChoice)
            choiceList = ['take', 'back up']
            choice = action(choiceList)
            if choice == 'take':
                print("You took the key! I bet there is a lock out there waiting for it!")
                user.addInv("journal key")
                self.goBed()
            elif choice == 'back up':
                self.goBed()
            else:
                print("You broke it!")
                self.goPillow()
        else:
            sceneOpen("You see the bottom of your stupid pillow and the place where a key used to be.")
            self.goBed()

    def goStand(self):
        sceneOpen("You see a glass of water.")
        print("Here are your options:")
        print("Drink the water | Don't drink the water")
        delay(dChoice)
        choiceList = ['drink', 'back up']
        choice = action(choiceList)
        if choice == 'drink':
            print("The water has been sitting here for a while. Are you sure?")
            delay(dChoice)
            choiceList = ['yes', 'no']
            choice = action(choiceList)
            if choice == 'yes':
                print("Are you really, really sure?")
                delay(dChoice)
                choiceList = ['yes', 'no']
                choice = action(choiceList)
                if choice == 'yes':
                    print("You drank the water. You have died of dysentery.")
                    gameOver(False)
                elif choice == 'no':
                    self.goStand()
                else:
                    print("You broke it!")
                    self.goStand()
            elif choice == 'no':
                self.goStand()
            else:
                print("You broke it!")
                self.goStand()
        elif choice == 'back up':
            self.goBed()
        else:
            print("You broke it!")
            self.goStand()

#Dresser Scene --------------------
class Dresser:
    def __init__(self):
        self.i = 0
    def goDresser(self):
        sceneOpen("You see dresser from IKEA.")
        print("Here are your options:")
        print("Look on top | Look in the upper drawer | Look in the bottom drawer")
        delay(dChoice)
        choiceList = ['top', 'upper', 'bottom', 'back up']
        choice = action(choiceList)
        if choice == 'top':
            self.goTopDresser()
        elif choice == 'upper':
            print("You open the drawer.")
            delay()
            self.goUpDrawer()
        elif choice == 'bottom':
            print("You open the drawer.")
            delay()
            self.goBotDrawer()
        elif choice == 'back up':
            h1.goHome()
        else:
            print("You broke it!")
            self.goDresser()

    def goTopDresser(self):
        if user.invCheck("journal") == False:
            sceneOpen("You see a few weeks worth of dust build-up and a journal.")
            print("Here are your options:")
            print("Take journal")
            delay(dChoice)
            choiceList = ['take', 'back up']
            choice = action(choiceList)
            if choice == 'take':
                print("You took the journal, but it has a lock on it!")
                user.addInv("journal")
                delay()
                self.goDresser()
            elif choice == 'back up':
                self.goDresser()
            else:
                print("You broke it!")
                self.goTopDresser()
        else:
            sceneOpen("You see a few weeks worth of dust build-up and a journal shaped clean spot.")
            self.goDresser()

    def goUpDrawer(self):
        sceneOpen("You see pants on one side and shirts on the other.")
        print("Here are your options:")
        print("Put on a shirt | Put on pants")
        delay(dChoice)
        choiceList = ['shirt', 'pants', 'shut']
        choice = action(choiceList)
        if choice == 'shirt':
            print(user.moreShirts())
            delay()
            self.goUpDrawer()
        if choice == 'pants':
            print(user.morePants())
            delay()
            self.goUpDrawer()
        elif choice == 'shut':
            self.goDresser()
        else:
            print("You broke it!")
            self.goUpDrawer()

    def goBotDrawer(self): #FINISH THIS
        opening = "You see a carefully arranged collection of junk in a drawer."
        print("Here are your options:")
        choiceFullText = "Admire the drawer"
        choiceList = ['admire', 'shut']
        if user.invCheck("lockbox") == False:
            choiceFullText += " | Take the lock box"
            choiceList += ["take box"]
            opening += "\nYou see a lock box on the left."
        if user.invCheck("screwdriver") == False:
            choiceFullText += " | Take the screwdriver"
            choiceList += ["take screwdriver"]
            opening += "\nYou see a screwdriver on the right."
        sceneOpen(opening)
        print(choiceFullText)
        delay(dChoice)
        choice = action(choiceList)
        if choice == 'take box':
            print("You took the lock box, but it is still locked!")
            user.addInv("lockbox")
            delay()
            self.goBotDrawer()
        elif choice == 'take screwdriver':
            print("You took the screwdriver. Maybe this can open a lock?")
            user.addInv("screwdriver")
            delay()
            self.goBotDrawer()
        elif choice == 'admire':
            sceneOpen("That sure is some nice junk!")
            self.goBotDrawer()
        elif choice == 'shut':
            self.goDresser()
        else:
            print("You broke it!")
            self.goBotDrawer()

#Window Scene --------------------
class Window:
    def __init__(self):
        self.i = 0
        self.look = {0:"You see a tree.", 1:"You still see a tree.", 2:"You see a really fat squirrel. On a tree."}
    def goWindow(self):
        sceneOpen("You see a window with a tree on the other side.")
        print("Here are your options:")
        choiceFullText = "Look by the bed | Look in the dresser | Look at the window | Check out the door"
        choiceList = ['look', 'open', 'back up']
        if user.invCheck("screwdriver") == True:
            choiceFullText += " | Try to pry open the window"
            choiceList += ["pry"]
        if user.invCheck("lockbox") == True:
            choiceFullText += " | Break the window"
            choiceList += ["break"]
        choice = action(choiceList)
        if choice == 'look':
            print(self.look[self.i])
            self.i = (self.i + 1) % 3
            delay()
            self.goWindow()
        elif choice == 'open':
            print("It's stuck shut!")
            delay()
            self.goWindow()
        elif choice == 'pry':
            print("The window only opened slightly, but you found a key! Totally normal hiding place.")
            delay()
            user.addInv("door key")
            user.dropInv("screwdriver")
            self.goWindow()
        elif choice == 'break':
            print("You threw the lock box through the window.")
            delay()
            print("You are FREEEEEEE!.. but your dad is piiiiiisssssssed....")
            gameOver(False)
        elif choice == 'back up':
            h1.goHome()
        else:
            print("You broke it!")
            self.goWindow()

#Desk Scene --------------------
class Desk:
    def __init__(self):
        self.i = 0

    def goDesk(self):
        sceneOpen("You see a desk with an open laptop computer.")
        print('You whisper to yourself, "This is a UNIX system. I know this."')
        delay()
        print("Here are your options:")
        print("Try to hack the door | Play Escape Your Room")
        choiceList = ['hack', 'play', 'back up']
        choice = action(choiceList)
        if choice == 'hack':
            print("You can only hack your door with a axe, Johnny.")
            delay()
            self.goDesk()
        elif choice == 'play':
            sceneOpen("Are you sure you want to start a new game?")
            choiceList = ['yes', 'no']
            choice = action(choiceList)
            if choice == 'yes':
                for c in "Loading":
                    time.sleep(.1)
                    print(c, end="")
                    sys.stdout.flush()
                for c in ('. '*10):
                    time.sleep(.5)
                    print(c, end="")
                    sys.stdout.flush()
                user.userReset()
                main()
            elif choice == 'no':
                self.goDesk()
            else:
                print("You broke it!")
                self.goDesk()
            choice = action(choiceList)
        elif choice == 'back up':
            h1.goHome()
        else:
            print("You broke it!")
            self.goDesk()

#Door Scene --------------------
class Door:
    def __init__(self):
        self.i = 0
    def goDoor(self):
        sceneOpen("You see a door. It used to be a tree.")
        print("Here are your options:")
        print("Try to open | Look through key slot")
        delay(dChoice)
        choiceList = ['open', 'look', 'back up']
        choice = action(choiceList)
        if choice == 'look':
            print("This is a new lock made since 1900. You can't see through it...")
            delay()
            self.goDoor()
        elif choice == 'open':
            if user.invCheck("door key") == True:
                print("You carefully insert the key into the door.")
                delay()
                print("The key turns...")
                delay()
                print("The door unlocks...")
                delay()
                print("The doorknob is cold to the touch...")
                delay()
                print("I bet you are supposed to turn this thing...")
                gameOver(True)
            else:
                print("It's locked!")
                delay()
                self.goDoor()
        elif choice == 'back up':
            h1.goHome()
        else:
            print("You broke it!")
            self.goDoor()

#Classes go here -------------------
user = Player()
h1 = Home()
b1 = Bed()
d1 = Dresser()
w1 = Window()
door = Door()
dsk = Desk()
#Main Function --------------------
def main():
    wipe(50, False)
    title = "\n  EEEEEEE                                     YY   YY                       RRRRRR                                \n  EE       sss    cccc   aa aa pp pp     eee  YY   YY  oooo  uu   uu rr rr  RR   RR  oooo   oooo  mm mm mmmm      \n  EEEEE   s     cc      aa aaa ppp  pp ee   e  YYYYY  oo  oo uu   uu rrr  r RRRRRR  oo  oo oo  oo mmm  mm  mm ::: \n  EE       sss  cc     aa  aaa pppppp  eeeee    YYY   oo  oo uu   uu rr     RR  RR  oo  oo oo  oo mmm  mm  mm     \n  EEEEEEE     s  ccccc  aaa aa pp       eeeee   YYY    oooo   uuuu u rr     RR   RR  oooo   oooo  mmm  mm  mm ::: \n           sss                 pp\n"
    print('~='*57)
    print(title)
    print('~='*57)
    print('\n'+ '-'*42 +' The Game: Exclamation Point! '+ '-'*42 +'\n')
    delay(4)
    #print("This is in build 0.0.0.0.a.dot.1, so most of the features don't work because we ran out of time.")
    #delay()
    print("Here is your backstory...")
    delay()
    print("You were doing absolutely nothing...")
    delay()
    print("But now you are in a room with a locked door.")
    delay()
    drama()
    delay()
    h1.goHome()


if __name__ == '__main__':
   main()
