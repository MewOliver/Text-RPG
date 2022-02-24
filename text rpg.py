import random
import time

playing = True
load_game = input("'continue' or 'new' ")
if load_game == 'new':
    name = input("Type characters name: ")
    choice = True
    while choice is True:
        try:
            _class = input("What class would you like to play, 'rogue', 'knight', 'viking': ")
            if _class == 'rogue':
                max_health = 60
                attack = 13
                reaction = 0.3
                trinket = 'experience dice'
            if _class == 'knight':
                max_health = 140
                attack = 5
                reaction = 0.2
                trinket = 'training shield'
            if _class == 'viking':
                max_health = 80
                attack = 15
                reaction = 0.1
                trinket = 'raising tooth'
            if _class == 'GOD':
                max_health = 10000000
                attack = 100
                reaction = 1
                trinket = 'godly lightning'
            choice = False
            ready_talk = False
            inventory = list()
            inventory.append(trinket)
        except:
            print("'type 'rogue', 'knight', 'viking'")
            continue

    # Player Stats
    level = 1
    hp = max_health
    exp = 0
    exp_required = 100
    damage = 0

elif load_game == 'continue':
    save_stats = list()
    lhand = open('save.txt')
    for i in lhand:
        line = i.rstrip()
        save_stats.append(line)
    name = str(save_stats[0])
    _class = str(save_stats[1])
    level = str(save_stats[2])
    max_health = str(save_stats[3])
    hp = max_health
    attack = str(save_stats[4])
    reaction = str(save_stats[5])
    exp = str(save_stats[6])
    exp_required = str(save_stats[7])
    trinket = str(save_stats[8])
    inventory = str(save_stats[9])
    
def display_stats():
    print('-----MY STATS--------------------------------------------------------')
    print('Name:', name)
    print('Class:', _class)
    print('Level:', str(level))
    print('Health:', str(hp) + '/' + str(max_health))
    print('Attack:', str(attack))
    print('Reaction:', str(reaction))
    print('Experience Points:', str(exp) + '/' + str(exp_required))
    print('Trinket:', str(trinket))
    print('---------------------------------------------------------------------')


def hub():
    print('-----------------')
    activity = input("What would you like to do 'stats', 'fight', 'talk', 'explore', 'save', 'equipment' or 'exit' ")
    if activity == 'stats':
        display_stats()
    elif activity == 'fight':
        fight()        
    elif activity == 'talk':
        talk() 
    elif activity == 'explore':
        explore()
    elif activity == 'save':
        save() 
    elif activity == 'equipment':
        equipment()
    elif activity == 'exit':
        playing = False
        quit()
       

def fight():
    global e_hp
    global enemy
    global e_attack
    global ready_talk
    global hp
    global exp
    global tut
    global trinket
    if tut == 'yes':
        ep = 5
        enemy = 'Egg'
        e_hp_max = 50
        e_attack = 0
    elif level == 1:
        ep = 100
        opponent = random.choice([1, 2, 3])
        if opponent == 1:
            enemy = 'Finch'
            e_hp_max = 120
            e_attack = 15
        elif opponent == 2:
            enemy = 'Robin'
            e_hp_max = 100
            e_attack = 20
        elif opponent == 3:
            enemy = 'Fantail'
            e_hp_max = 80
            e_attack = 25
            
    elif level == 2:
        ep = 100
        opponent = random.choice([1, 2, 3])
        if opponent == 1:
            enemy = 'Chicken'
            e_hp_max = 130
            e_attack = 17
        elif opponent == 2:
            enemy = 'Sparrow'
            e_hp_max = 110
            e_attack = 22
        elif opponent == 3:
            enemy = 'Dove'
            e_hp_max = 90
            e_attack = 27
    
    elif level == 3:
        ep = 100
        opponent = random.choice([1, 2, 3])
        if opponent == 1:
            enemy = 'Duck'
            e_hp_max = 140
            e_attack = 19
        elif opponent == 2:
            enemy = 'Pheasant'
            e_hp_max = 120
            e_attack = 24
        elif opponent == 3:
            enemy = 'Starling'
            e_hp_max = 100
            e_attack = 29
            
    elif level == 4:
        ep = 100
        opponent = random.choice([1, 2, 3])
        if opponent == 1:
            enemy = 'Owl'
            e_hp_max = 150
            e_attack = 21
        elif opponent == 2:
            enemy = 'Woodpecker'
            e_hp_max = 130
            e_attack = 26
        elif opponent == 3:
            enemy = 'Parrot'
            e_hp_max = 110
            e_attack = 31
    
    elif level == 5:
        ep = 150
        opponent = random.choice([1, 2, 3])
        if opponent == 1:
            enemy = 'Rooster'
            e_hp_max = 220
            e_attack = 20
        elif opponent == 2:
            enemy = 'Bin Chicken'
            e_hp_max = 160
            e_attack = 28
        elif opponent == 3:
            enemy = 'Raven'
            e_hp_max = 120
            e_attack = 35
                   
    print("An agressive,", enemy, "appears, get ready to fight")
    combo = 0
    e_hp = e_hp_max
    while e_hp > 0:
        action = input("What do you want to do (type 'attack'): ")
        if action == 'attack':
            print('-----------------')
            fighting = True
            while fighting is True:
                try:
                    swing = input('Press enter to attack ')
                    if swing == '':
                        damage = random.randrange(int(attack - 5), int(attack + 5))
                        at = (random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9))
                        for x in range(1):
                            print(at, end='\r')
                            time.sleep(float(reaction))           
                        answer = list()
                        print('                                                                               ')
                        x = 0
                        dice = 0
                        for i in at:
                            answer.append(input('type a number: '))
                            if int(answer[x]) == int(at[x]):
                                x = x + 1
                                damage = damage + int(random.randint(3,7))
                                combo = combo + 1
                                if trinket == 'experience dice':
                                    dice = dice + 2
                            elif int(answer[x]) != int(at[x]):
                                fighting = False
                                if trinket == 'experience dice':
                                    exp  = exp + dice
                                    print('The experince dice granted', dice, 'exp')
                                    print(exp, '/',  exp_required)
                                break
                except:
                    print('Invalid input, try again')
                    continue
            if trinket == 'charm of combo':
                damage = int(damage) + (combo)
                print('Your combo is', combo)
            if trinket == 'charm of force' and e_hp == e_hp_max:
                damage = int(damage)*2
            e_hp = int(e_hp) - int(damage)
            print('-----------------')
            print('You dealt', damage, 'damage' )
            if e_hp > 0:
                print(enemy, 'has', e_hp, 'health remaining')
                e_damage = random.randrange(int(e_attack - 5), int(e_attack + 5))
                if e_damage <= 0:
                    e_damage = 0
                    print ('The', enemy, 'misses with grace')
                else:
                    print(enemy, 'strikes back, dealing:', str(e_damage), 'damage')
                hp = hp - e_damage
                if trinket == 'charm of vigor':
                    print('You restored', int(int(damage)/2/2), 'health')
                    hp = hp + int(int(damage)/2/2)
                print(name, 'has', str(hp) + '/' + str(max_health), 'remaining')
                print('-----------------')
                if hp <= 0:
                    print('YOU DIED')
                    input("")
                    quit()
            else:
                print('-----------------')
                print('The', enemy, 'is dead, congratulations!')
                if trinket == 'traning shield':
                    exp = exp + hp
                    print ('Your traning shield granted you a bonus', hp, 'exp')
                hp = max_health
                if trinket == 'raising tooth':
                    overkill_exp = (10*(+abs(e_hp)))
                else:
                    overkill_exp = (+abs(e_hp))
                exp = exp + int(overkill_exp)
                print('You gained a bonus', str(overkill_exp), 'exp for overkill')
                print('-----------------')
                gain_exp (ep)
                ready_talk = True

def gain_exp (ep):
    global exp
    global level
    global attack
    global max_health
    global exp_required
    global hp
    global reaction
    print('You gained', ep, 'experince points')
    exp = exp + ep
    if exp >= exp_required:
        level = int(level) + 1
        exp = int(exp) - int(exp_required) 
        exp_required = int(exp_required) + 50  
        print('Level Up! You are now level:', level,)
        choice = True
        while choice is True:
            increase = input("You can increase your attack or health by typing 'reaction', 'attack' or 'health' ")
            if increase == 'attack':
                attack = attack + 5
                choice = False
                display_stats()
            elif increase == 'health':
                max_health = max_health + 20
                hp = max_health
                choice = False
                display_stats()
            elif increase == 'reaction':
                reaction = reaction + 0.10
                choice = False
                display_stats()
    else:
        print('current exp:', str(exp) + '/' + str(exp_required))

def talk():
    global ready_talk 
    if ready_talk is True:
        conversation = random.randint(1, 3)
        if conversation == 1:
            print('-----------------')
            print("AaAaAaAaAaAaAaA, I'm scareeeeed. The deep cave is full of it")
            print("Somehow the more of it there is, the less I see... Its terrifying")
            print("Please go to the cave and find this for me and expel it")
            ready_talk = False
        if conversation == 2:
            print('-----------------')
            print("Sorry, young fellow, how goes it")
            print("I have been told that such a thing exists that goes up but doesnt come down again")
            print("An old bird in the city is trying to figure it out, please help him, thanks")
            ready_talk = False
        if conversation == 3:
            print('-----------------')
            print("Hi, my name is Hallant. Im loving life!")
            print("My parents are amazing, being able to look after three kids at the same time")
            print("Bink and Dreeb are a bit of a handful but I heard the third one is cool")
            print("Can you find my parents in the forest and tell them the name of their third kid, thanks!")
            ready_talk = False
    else:
        print('No one is ready to talk')

def equipment():
    global view
    global trinket
    print(inventory)
    choice = True
    while choice is True:
        view = input('What would you like to look at closer: ') 
        if view == 'training shield' and view in inventory:
            print('-----------------')
            print('When this is equiped, your remaining health will be turned into exp after a battle')
            choice = False
            change_trinket()     
        elif view == 'raising tooth' and view in inventory:
            print('-----------------')
            print('When this is equiped, the bonus exp awarded for overkill is multiplied by 10')
            choice = False
            change_trinket()
        elif view == 'experience dice' and view in inventory:
            print('-----------------')
            print('When this is equiped, for every correct number during a battle gain 2 exp')
            choice = False
            change_trinket()
        elif view == 'useless ring' and view in inventory:
            print('-----------------')
            print('When this is equiped, it does nothing... or does it???????')
            choice = False
            change_trinket()
        elif view == 'charm of combo' and view in inventory:
            print('-----------------')
            print('When this is equiped, every correct number adds an additional damage')
            choice = False
            change_trinket()
        elif view == 'charm of vigor' and view in inventory:
            print('-----------------')
            print('When this is equiped, a quarter of the damage delt in restored as health')
            choice = False
            change_trinket()
        elif view == 'charm of force' and view in inventory:
            print('-----------------')
            print('When this is equiped, Your first attack does 2x damage')
            choice = False
            change_trinket()
        else:
            print('Not an item in inventory')
        
def change_trinket():
    global view
    global trinket
    choice = True
    while choice is True:
        change_equip = input('Would you like to equip ' + view + '? ')
        if change_equip == 'yes':
            trinket = view
            print(trinket, 'sucessfully equiped')
            choice = False
        elif change_equip == 'no':
            trinket = 'none'
            print('No trinket equiped')
            choice = False
        else:
            print('Type yes or no')
        
def explore():
    if level == 1 and 'useless ring' not in inventory:
        print('You walk around the town and see a shining object on the ground')
        print('You found a useless ring')
        inventory.append('useless ring')
   
    elif level > 1:
        location = input("Would you like to explore ('cave') ('forest') ('city') ")
        if location == 'cave':
            if level >= 3 and 'charm of combo' not in inventory:
                answer = input("what is the ever growing presence in this cave? (all answers are one-word lower case) ")
                if answer == 'darkness':
                    print('You found the charm of combo')
                    inventory.append('charm of combo')
                else:
                    print('That is incorrect')
            else:
                print('Cave has been explored... for now')
                
        elif location == 'forest':
            if level >= 3 and 'charm of force' not in inventory:
                answer = input("What was the name of the families third child? (all answers are one-word lower case) ")
                if answer == 'hallant' or answer == 'Hallant':
                    print('You found the charm of force')
                    inventory.append('charm of force')
                else:
                    print('That is incorrect')
            else:
                print('Forest has been explored... for now')
                
        elif location == 'city':
            if level >= 3 and 'charm of vigor' not in inventory:
                answer = input("An old bird is perplexed, help him out, answer his question? (all answers are one-word lower case) ")
                if answer == 'age':
                    print('You found the charm of vigor')
                    inventory.append('charm of vigor')
                else:
                    print('That is incorrect')
            else:
                print('Forest has been explored... for now')
    
    
def save():
    print('GAME SAVED')
    a_list = [str(name), str(_class), str(level), str(max_health), str(attack), str(reaction), str(exp), str(exp_required), str(trinket), str(inventory)]
    textfile = open("save.txt", "w")
    for element in a_list:
        textfile.write(element + "\n")
    save_stats = list()
    lhand = open('save.txt')
    for i in lhand:
        line = i.rstrip()
        save_stats.append(line)
    
display_stats()
#Tutorial
if load_game == "new":
    choice = True
    while choice is True:
        tut = input('Would you like to play the tutorial (yes or no): ')
        if tut == 'yes':
            choice = False
            print('To give you a fighting chance I have devised an intense training fight against, an, AN, EGG!!!')
            print('right now the only way to interact with an opponate is through an attack')
            print('Do this by typing attack, then when you are ready to swing press enter')
            print('When you start a swing a random set of numbers will flash up on the screen')
            print('In order to deal damage you must remember and repeat these numbers one at a time, the more you get right, the more damage')
            print("Alright I'll start the fight, good luck")
            print('-----------------')
            fight()

            display_stats()
            print('Well done, you learn quickly')
            input('Press enter to continue')
            print('-----------------')
            print('In the game you have many options; fighting crazed birds, talking to towns folk, exploring deep landscapes')
            print('fight: enter into to combat with an opponate with the chance for victory and exp')
            print('talk: talk to the birds of the nest to gain useful information and create powerful bonds')
            print('explore: go to different locations to plunder for loot, danger might lurk within')
            print('equipment: change your equipment to gain an advantage')
            print('-----------------')
            tut = None
            continue
        elif tut == 'no':
            input('Press enter to continue')
            choice = False


while playing is True:
    hub()
    
input('Press enter to continue')