# - random factors: lose clothes in river, bad weather delays, food spoils, find food or abandoned supplies
#c5: river- if you choose the wrong option, (i.e., you realize that you don't know how to swim, or lose your clothes) you DIE
#c6 (at 0): you're alive! if you have enough money left, you can take the boat home, if you don't, you realize you will have to survive on the island for eternity

#introduction
print("""ISLAND ADVENTURE
~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~
YOU WAKE UP ON A DESERTED ISLAND. YOUR GOAL IS TO MAKE IT TO THE OTHER SIDE OF THE ISLAND,
WHERE THERE ARE SHIPS THAT CAN TAKE YOU HOME, IN THE SHORTEST AMOUNT OF TIME POSSIBLE.
GOOD LUCK (YOU'RE GONNA NEED IT).""")

#creating a character using a class
class Character(object):
        """Character class"""
        # initializing the character
        def __init__(self, name):
            self.name = name
            #storing the inventory in a dictionary
            self.inventory = {
            'food': 0,
            'clothes': 2,
            'money': 50}
            #starting statuses, a set value before the game starts
            self.day = 1
            self.distance_left = 10
            self.total_distance = 50
            self.health = 100
            print(f"""Welcome, {name}. You wake up with only the clothes on your back and $50 in your pocket.""")
        # if this function is called, the inventory will be printed
        def list_inventory(self):
            # will be printed in this format using a for loop
            for k, v in self.inventory.items():
                print(f"""{k} --- {v}""")
        # if this function is called, the status will be printed
        def list_status(self):
            print(f""" \n
            Day --- {self.day}
            Distance until next checkpoint --- {self.distance_left}
            Health --- {self.health} \n
            """)
        # the character walks forward, and different scenario occurs at each distance
        def list_walk(self, miles = 5):
            self.distance_left -= miles
            self.total_distance -= miles
            self.day += 1
            #food decreases with each day
            if self.inventory['food'] > 0:
                self.inventory['food'] -= 2
            #health decreases each time you walk
            if self.health > 0:
                self.health -= 2
            print(f"""

            Day: {self.day} --- Next Checkpoint in: {self.distance_left} miles

            """)


#defining the character
a = Character(input("""What is your name? \n - """))

#Checkpoints (every 10 miles) are stored in a list
checkpoints = [50, 40, 30, 20, 10, 0]
#defining a function
def ckpt1():
    #The options are chosen by the user and are stored as a variable
    #it also turns the user's input into an int (instead of a string) so that it can be used later
    b = int(input(f"""What would you like to do?
1. Inventory
2. Status
3. Go forward (miles left: {a.distance_left})\n - """))
#using if and elif statements to have different options and results
    if b == 1:
        a.list_inventory()
        ckpt1()
    elif b == 2:
        a.list_status()
        ckpt1()
    elif b == 3:
        a.list_walk()
    #If the user types in a value that isn't listed, the block of code will repeat instead of having an error
    else:
        print("""invalid input.""")
        ckpt1()

#The function is called once the total distance reaches 50
if a.total_distance == 50:
    ckpt1()

#defining another function that is a store
def store1():
    d = int(input("""
            1. food --- $1 per pound
            2. clothes --- $3 per piece
            3. stay overnight --- $10
            4. leave the hut \n - """))
    #checks the user's input and runs a block of code based on it
    if d == 1:
        pounds = int(input("How many pounds? (will be rounded to the nearest whole #) \n - "))
        #The user chooses amount of food they want to buy, and its cost is calculated automatically
        cost_f = pounds * 1
        #Also, the amount of food in the inventory is changed based on how much they buy
        a.inventory['food'] += pounds
        #The cost is subtracted from the amount of money in the inventory
        a.inventory['money'] -= cost_f
        print(f"""\n You bought {pounds} pounds of food. You now have {a.inventory['money']} dollars.\n """)
        #The function also runs again in case you want to buy something else
        store1()
    elif d == 2:
        #Runs the same way as the block of code above, except with clothes
        pieces = int(input("How many? (will be rounded to the nearest whole #) \n - "))
        cost_c = pieces * 3
        a.inventory['clothes'] += pieces
        a.inventory['money'] -= cost_c
        print(f"""\n You bought {pieces} pieces of clothing. You now have {a.inventory['money']} dollars. \n""")
        store1()
    elif d == 3:
        #If staying overnight, it will be the next day
        a.day += 1
        #Health is reset to 100 because you rested
        a.health = 100
        #Costs $10 to stay, so this amount is subtracted from money
        a.inventory['money'] -= 10
        print(f"""\n You stayed in the sketchy hut overnight. Even though the bed was made of hay, you feel rested.
        It is now Day {a.day}. You have {a.inventory['money']} dollars left.\n """)
        #prints the player's status automatically to inform them that it is the next day
        a.list_status()
        a.distance_left = 10
        #returns to the ckpt1 function so that the player can still buy anything else they want
        ckpt1()
    elif d == 4:
        a.distance_left = 10
        a.list_walk()
    else:
        print("""invalid input. try again \n - """)
        store1()

#defining the next function
def ckpt2():
    c = int(input("""You approach the edge of the dense forest.
    On the outskirts of the trees seems to be a sketchy hut with an old man sitting in a lawn chair outside it.
    What do you do?
    1. Inventory
    2. Status
    3. Approach the sketchy vendor
    4. Keep on walking - you don't want to cause any trouble \n - """))
    if c == 1:
        a.list_inventory()
    elif c == 2:
        a.list_status()
    elif c == 3:
        print("You slowly walk towards the vendor, and he greets you with a smile.\n 'Would you like to buy something?' he says. 'Here are my prices:'")
        #the store function is called, which was created earlier
        store1()
    elif c == 4:
        a.list_walk()
    else:
        print("""invalid input. try again \n - """)
        ckpt2()

while a.total_distance == 45:
    print("You have no food and are starving.\nYour health is now 90.")
    #health is reset to 90
    a.health = 90
    #calls the first checkpoint function
    ckpt1()

while a.total_distance == 40:
    ckpt2()

#checks if total distnace is 35 and if the user has food in their inventory - results in diff outcomes
if a.total_distance == 35 and a.inventory['food'] == 0:
    print("You went too long without food. You have died of starvation. :( \n ***THE END***")

if a.total_distance == 35 and a.inventory['food'] > 0:
    ckpt1()

def ckpt3():
    a.distance_left = 10
    a.health -= 10
    d = int(input(f"""
    1. Inventory
    2. Status
    3. Stop to rest
    4. Keep going (miles left: {a.distance_left}\n - """))
    if d == 1:
        a.list_inventory()
        ckpt3()
    elif d == 2:
        a.list_status()
        ckpt3()
    elif d == 3:
        #The user inputs how long they want to rest
        days = int(input("How many days?\n - "))
        #based on this response, the status is altered
        a.day += days
        #health increases by 5 * each day
        a.health += days * 5
        print(f"You rested for {days} days. You feel much better and it has gotten warmer.")
        #automatically prints status
        a.list_status()
        ckpt3()
    elif d == 4:
        a.distance_left = 10
        a.list_walk()
    else:
        print("""invalid input. try again \n - """)
        ckpt3()

#Checks the distance and how much food and clothing the user has
if a.total_distance == 30 and a.inventory['clothes'] <= 2 and a.inventory['food'] > 0:
    print("""The temperature has dropped over 30 degrees and it has started to snow.
    You realize that you are shivering and forgot to buy another piece of clothing, like a jacket, at the vendors hut.
    Throughout the course of the day, you develop hypothermia and die. :(
    ***THE END***""")
#uses if statements to check each one
if a.total_distance == 30 and a.inventory['clothes'] > 2 and a.inventory['food'] == 0:
    a.health -= 10
    print(f"You have no food and are starving. Your health is now {a.health}")
if a.total_distance == 30 and a.inventory['clothes'] > 2 and a.inventory['food'] > 0:
    print("""The temperature has dropped over 30 degrees and it has started to snow.
    Luckily, you have a warm jacket that you bought from the sketchy vendor.
    Even though you are freezing, you are still able to survive.
    What would you like to do?""")
    ckpt3()

#defining a function to be used later
def hunt():
    #importing the random module to be used later on
    import random
    h = int(input("""Choose your weapon:
    1. Bow and Arrows
    2. Rifle
    3. Knife
    4. Sheer luck\n - """))
    if h == 1:
        #if 1 is typed, the random module will choose a random number between 0 and 15, not including 0
        g = random.randint(0,15)
        #Based on what random number is chosen, that amount of food is added to inventory
        a.inventory['food'] += g
        #informs the user of the amount of food collected
        print(f"You have chosen to hunt. You have killed a deer and collected {g} pounds of food. Congrats!")
        print(f"You now have {a.inventory['food']} pounds of food.")
    elif h == 2:
        #if 2 is typed, the random module will choose a random number between 0 and 20, not including 0 (increases the chance of getting a higher number)
        i = random.randint(0,20)
        a.inventory['food'] += i
        print(f"You have chosen to hunt. You have killed a deer and collected {i} pounds of food. Congrats!")
        print(f"You now have {a.inventory['food']} pounds of food.")
    elif h == 3:
        #runs the same way as the blocks of code above
        j = random.randint(0,10)
        a.inventory['food'] += j
        print(f"You have chosen to hunt. You have killed a rabbit and collected {j} pounds of food. Congrats!")
        print(f"You now have {a.inventory['food']} pounds of food.")
    elif h == 4:
        #runs the same way as the blocks of code above
        k = random.randint(0,5)
        a.inventory['food'] += k
        print(f"You have chosen to hunt. You have managed to catch a squirrel and collected {k} pounds of food. Congrats!")
        print(f"You now have {a.inventory['food']} pounds of food.")
    else:
        #otherwise, the hunt function is called again
        print("""invalid input. try again \n - """)
        hunt()

def ckpt4():
    #resets the distance left to 10, to avoid getting a negative distance left
    a.distance_left = 10
    e = int(input(f"""
    1. Inventory
    2. Status
    3. Stop to rest
    4. Hunt for food
    5. Keep going (miles left: {a.distance_left} \n - """))
    if e == 1:
        a.list_inventory()
    elif e == 2:
        a.list_status()
    elif e == 3:
        #the user inputs an amount of days that is used to recalculate the health and day
        f = int(input(""""How many days would you like to rest?
        Your health will increase by 5 for every night you rest.\n - """))
        a.day += f
        a.health += f * 5
        #informs the user of what they chose
        print(f"""You rested for {f} days. You feel ready to continue your journey.""")
        a.list_status()
    elif e == 4:
        #hunt function is called if the user chooses to do so
        hunt()
    #checks to make sure the user has enough food before walking
    elif e == 5 and a.inventory['food'] > 0:
        a.list_walk()
    #if they do not, the game ends
    elif e == 5 and a.inventory['food'] == 0:
        print("You have run out of food and come down with dysentery.\n You have died. :(\n ***THE END***")
    else:
        print("""invalid input. try again \n - """)
        ckpt4()

#makes sure the user has food before continuing
if a.total_distance == 25 and a.inventory['food'] == 0:
    print("You went too long without food. You have died of starvation. :( \n ***THE END***")

if a.total_distance == 25 and a.inventory['food'] > 0:
   ckpt1()

if a.total_distance == 20 and a.inventory['food'] > 0:
    print("""You have made it past the mountain range. Surprisingly, you feel hopeful.
    You reach a small clearing in the forest.
    You have {a.inventory['food']} pounds of food left. What would you like to do?""")
    #calls the ckpt4 function, defined earlier
    ckpt4()

if a.total_distance == 20 and a.inventory['food'] == 0:
    #The game ends if the player has no food
    print("You have run out of food and come down with dysentery.\n You have died. :(\n ***THE END***")

def ckpt5():
    l = int(input("""
    1. Try to swim across
    2. Hop on the rocks all the way across"""))
    if l == 1:
        print("You try to swim across, except you realize that you don't know how to swim. \n You drown. :( \n ***THE END***")
    elif l == 2:
        print("""You carefully jump from rock to rock. \n Unfortunately, on the last rock, you slip and fall into the cold water. \n
        You manage to barely make it to shore, but because the water was so cold you get hypothermia. Your health decreases by 50.""")
        a.health -= 50
        a.status()
    else:
        print("invalid input. try again \n - ")
        ckpt5()

if a.total_distance == 10 and a.inventory['food'] > 0 and a.health > 0:
    ckpt1()

if a.total_distance == 10 and a.inventory['food'] == 0 and a.health == 0:
    print("Even though you survived the river, you are too weak to continue. You die of hypothermia. :( \n ***THE END***")

if a.total_distance == 10 and a.inventory['food'] > 0 and a.health == 0:
    print("Even though you survived the river, you are too weak to continue. You die of hypothermia. :( \n ***THE END***")

if a.total_distance == 10 and a.inventory['food'] == 0 and a.health > 0:
    print("Even though you survived the river, you have run out of food. You die of starvation. :( \n ***THE END***")


if a.total_distance == 0 and a.inventory['food'] > 0 and a.health > 0:
    print(f"""You finally have reached the edge of the forest. You can see a fishing community ahead. \n
    You run up to the docks, and the fisherman there is willing to give you a ride home.
    WHOOPTY DOOOOOOOOOOO!!!!
    YOU DID IT!!!!!!
    YOU SURVIVED!!!!!!!
    YOU AIN'T DEDDDDDDD!!!!!!!!
    🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥

    -----------------------------
    END RESULTS:
    It took you: {days} Days
    -----------------------------
    Created by: Betia Zeng
    End credits: Anonymous Donor
    Thanks for playing!""")

if a.total_distance == 10 and a.inventory['food'] == 0 and a.health == 0:
    print("Even though you survived the river, you are too weak to continue. You die of hypothermia. :( \n ***THE END***")

if a.total_distance == 10 and a.inventory['food'] > 0 and a.health == 0:
    print("Even though you survived the river, you are too weak to continue. You die of hypothermia. :( \n ***THE END***")

if a.total_distance == 10 and a.inventory['food'] == 0 and a.health > 0:
    print("Even though you survived the river, you have run out of food. You die of starvation. :( \n ***THE END***")

# FIGURE OUT THE INVALID PROBLEM


