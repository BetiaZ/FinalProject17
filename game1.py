# - have checkpoints where you can rest
# - can die of starvation, disease, or drowning
# - can hunt (random pounds of food), set how many miles you want to go per day
# - goal: get to the end in the shortest number of days possible
# - random factors: lose clothes in river, bad weather delays, food spoils, find food or abandoned supplies
#checkpoint 2: really cold, die if you don't have clothes
#c3: store again
#c4: river- if you choose the wrong option, (i.e., you realize that you don't know how to swim, or lose your clothes) you DIE
#c5: you're alive! if you have enough money left, you can take the boat home, if you don't, you realize you will have to survive on the island for eternity

#introduction
print("""ISLAND ADVENTURE
~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~
YOU WAKE UP ON A DESERTED ISLAND. YOUR GOAL IS TO MAKE IT TO THE OTHER SIDE OF THE ISLAND,
WHERE THERE ARE SHIPS THAT CAN TAKE YOU HOME, IN THE SHORTEST AMOUNT OF TIME POSSIBLE.
GOOD LUCK (YOU'RE GONNA NEED IT).""")

#creating a character
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
            #starting statuses
            self.day = 1
            self.distance_left = 10
            self.total_distance = 50
            self.health = 100
            print(f"""Welcome, {name}. You wake up with only the clothes on your back and $50 in your pocket.""")
        # if this function is called, the inventory will be printed
        def list_inventory(self):
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
            print(f"""

            Day: {self.day} --- Next Checkpoint in: {self.distance_left} miles

            """)


#defining the character
a = Character(input("""What is your name? \n - """))

checkpoints = [50, 40, 30, 20, 10, 0]
def ckpt1():
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
    else:
        print("""invalid input.""")
        ckpt1()

if a.total_distance == 50:
    ckpt1()

def store1():
    d = int(input("""You slowly walk towards the vendor, and he greets you with a smile.
        'Would you like to buy something?' he says. 'Here are my prices:'
            1. food --- $1 per pound
            2. clothes --- $3 per piece
            3. stay overnight --- $10
            4. leave the hut \n - """))
    if d == 1:
        pounds = int(input("How many pounds? (will be rounded to the nearest whole #) \n - "))
        cost_f = pounds * 1
        a.inventory['food'] += pounds
        a.inventory['money'] -= cost_f
        print(f"""\n You bought {pounds} pounds of food. You now have {a.inventory['money']} dollars.\n """)
        store1()
    elif d == 2:
        pieces = int(input("How many? (will be rounded to the nearest whole #) \n - "))
        cost_c = pieces * 3
        a.inventory['clothes'] += pieces
        a.inventory['money'] -= cost_c
        print(f"""\n You bought {pieces} pieces of clothing. You now have {a.inventory['money']} dollars. \n""")
        store1()
    elif d == 3:
        a.day -= 1
        a.health = 100
        a.inventory['money'] -= 10
        print(f"""\n You stayed in the sketchy hut overnight. Even though the bed was made of hay, you feel rested.
        It is now Day {a.day}. You have {a.inventory['money']} dollars left.\n """)
        a.list_status()
        break
    elif d == 4:
        a.distance_left = 10
        a.list_walk()
    else:
        print("""invalid input. try again \n - """)
        store1()
#first scenario occurs after walking the first time, or when the total distance left is 45
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
        store1()
    elif c == 4:
        a.list_walk()
    else:
        print("""invalid input. try again \n - """)
        ckpt2()

while a.total_distance == 45:
    print("You have no food and are starving.\nYour health is now 90.")
    a.health = 90
    ckpt1()

while a.total_distance == 40:
    ckpt2()

if a.total_distance == 35 and a.inventory['food'] == 0:
    print("You went too long without food. You have died of starvation. :( \n ***THE END***")

if a.total_distance == 35 and a.inventory['food'] > 0:
    a.distance_left = 10
    ckpt1()
#you forgot to buy another piece of clothing, like a jacket, at the vendor's hut
#MAKE SURE TO PUT A LIMIT WHEN MONEY > 0

