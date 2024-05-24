import random
import time
import os
import string

professions = ["Woodcutter", "Miner", "Fisherman", "Herbalist"]

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.inventory = Inventory()
        self.actions_left = 3
        self.days_survived = 0
        self.hunger = 0
        
    def set_profession(self, profession):
        self.profession = profession
    
    def main_hand(self, mainhand):
        self.mainhand = mainhand

class Inventory:
    def __init__(self):
        self.resources = {'meal': 0, 'iron ingot': 10}
        self.currencies = {'gold':6}
        self.weapons = []
        

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def add_currency(self, currency, amount):
        self.resources.setdefault(currency, 0)
        self.currencies[currency] += amount

    def add_resource(self, resource, amount):
        self.resources.setdefault(resource, 0)
        self.resources[resource] += amount

class Loot:
    def loot_target(self, target):
        print(len(target.inventory.weapons))
        print(len(target.inventory.currencies))
        print(len(target.inventory.resources))

def player_input(prompt, options, style, menu = None, print_options = True):
    assert options, "no options given"
    while True:
        if menu is not None:
            print(menu)

        print(f"{prompt}:")
        if style == "shop":
            for i, option in enumerate(options, start=0):
                if print_options:
                    print(f"{i:} {option}")

        elif style == "weapons":
            n = 1
            extender = [0]
            options.extend(extender)
            if print_options:
                for weapon in options:
                    if weapon == 0:
                        print(f"{n:} Back")
                    elif weapon == game.player.main_hand:
                        print(f"{n:} {weapon.quality} {weapon.name} is worth {weapon.value} that does {weapon.damage} damage (Current Mainhand)")
                        n += 1
                    else:
                        print(f"{n:} {weapon.quality} {weapon.name} is worth {weapon.value} that does {weapon.damage} damage")
                        n += 1

        else:
        
            for i, option in enumerate(options, start=1):
                if print_options:
                    print(f"{i:} {option}")

        try:
            chosen = (int(input()))
        except ValueError:
            os.system("cls")
            input("Invalid option.")
            os.system("cls")
            continue

        if style == "index":
            if 0 < chosen <= len(options):
                os.system("cls")
                chosen -= 1
                return chosen
            else:
                os.system("cls")
                input("Invalid option.")
                os.system("cls")

        if style == "int":
            if 0 < chosen <= len(options):
                    os.system("cls")
                    return chosen
            else:
                os.system("cls")
                input("Invalid option.")
                os.system("cls")

        if style == "shop":
            if 0 <= chosen <= len(options):
                    os.system("cls")
                    return chosen
            else:
                os.system("cls")
                input("Invalid option.")
                os.system("cls")
                
        if style == "weapons":
            if 0 < chosen <= len(options):
                    os.system("cls")
                    chosen -= 1
                    return chosen
            else:
                os.system("cls")
                input("Invalid option.")
                os.system("cls")

def player_input_string(prompt):
    while True:
        os.system("cls")
        print(f"{prompt}:")
        name = input()


        if len(name) < 4:
            os.system("cls")
            print("This name is too short!")
            print(input("Press Enter to continue..."))
            os.system("cls")
            continue

        if len(name) > 20:
            os.system("cls")
            print("This name is too long!")
            print(input("Press Enter to continue..."))
            os.system("cls")
            continue

        for char in name:
            if char in string.digits:
                os.system("cls")
                print("Your name cannot contain a number!")
                print(input("Press Enter to continue..."))
                os.system("cls")
                break
        
        else:
            os.system("cls")
            return name
            
def wait_for_enter():
    print(input("Press Enter to continue..."))
    os.system("cls")

def is_Target_dead(self):
    if self.health <= 0:
        return True
    else:
        return False

def onStartup():
    global professions

    print(" ____  _            _                  _ _   _     ")
    print("| __ )| | __ _  ___| | _____ _ __ ___ (_) |_| |__  ")
    print("|  _ \| |/ _` |/ __| |/ / __| '_ ` _ \| | __| '_ \ ")
    print("| |_) | | (_| | (__|   <\__ \ | | | | | | |_| | | |")
    print("|____/|_|\__,_|\___|_|\_\___/_| |_| |_|_|\__|_| |_|")
    print()
    wait_for_enter()

    print("You will live the simple life of a blacksmith.")
    print("Work, craft items, and sell them to make money needed to survive.")
    wait_for_enter()

    print("Before you begin, we need to figure out who you are!")
    wait_for_enter()

    player = player_input_string("What would you like to be called?")

    print(f"Its been decided, you will be called {player} from here on out!")
    wait_for_enter()

    print("Besides just being a blacksmith, you also have the chance to choose a second profession.")
    print("What will you choose?")
    wait_for_enter()

    os.system("cls")
    options = [
        "Woodcutter",
        "Miner",
        "Fisherman",
        "Herbalist"
    ]
    profession_index = player_input("Please choose a secondary profession:", options, "index")
    professions = ["Woodcutter", "Miner", "Fisherman", "Herbalist"]

    player_profession = professions[profession_index]

    print(f"So you've chosen to be a {player_profession}, good choice!")
    wait_for_enter()

    print(f"Let the story of {player} the Blacksmith unfold")
    print("Try to survive as long as you can.")
    wait_for_enter()
    return player, player_profession

def crafting(player):
    game.player.actions_left -= 1
    newly_crafted = Weapon.craft_weapon()
    ingots_used = random.randint(1,3)

    if ingots_used > game.player.inventory.resources['iron ingot']:
        print(f"While trying to craft a new item, you ran out of iron ingots. You only had {game.player.inventory.resources['iron ingot']} iron ingots.")
        print(f"But the craft was going to consume {ingots_used}. Sadly you won't be able to finish the craft and the ingots went to waste.")
        game.player.inventory.resources['iron ingot'] = 0
        print()
        wait_for_enter()
        return
        

    print("You decided to craft an item of unknown quality...")
    print(f"After many hours, you manage to craft a {newly_crafted.quality} {newly_crafted.name} that does {newly_crafted.damage} damage worth {newly_crafted.value} gold coins!")
    print(f"You used {ingots_used} iron ingots in the process.")
    print()

    options = [
        "Sell",
        "Keep"
    ]
    choice = (player_input("What would you like to do?", options, "index", menu = f"Would you like to sell it for {newly_crafted.value} or add it to your inventory?")+1)
    os.system("cls")

    print(choice)

    if choice == 1:
        print(f"You sold the {newly_crafted.quality} {newly_crafted.name} for {newly_crafted.value} gold pieces.")
        game.player.inventory.add_currency('gold', newly_crafted.value)
        game.player.inventory.resources['iron ingot'] -= ingots_used
        print(f"You now have {game.player.inventory.currencies['gold']} gold coins!")
        print()
        print(input("Press Enter to continue..."))
        os.system("cls")
        

    elif choice == 2:
        print(f"You decided the keep the {newly_crafted.quality} {newly_crafted.name}.")
        game.player.inventory.add_weapon(newly_crafted)
        game.player.inventory.resources['iron ingot'] -= ingots_used
        print(f"You now have {len(game.player.inventory.weapons)} weapons in your inventory")
        print(input("Press Enter to continue..."))
        os.system("cls")
        
def shop():

        print("Welcome to the store! Spend your hard earned currency here!")
        print(f"You currently have {game.player.inventory.currencies['gold']} to spend:")
        print("")

        options = [
            "Buy iron ingot(s)",
            "Buy meal(s)",
            "Sell Weapons",
            "Back"
        ]

        choice = player_input("What would you like to do?", options, "int")
        os.system("cls")
    #iron ingots
        if choice == 1:
            cost = 2
            options = []
            amount = int(game.player.inventory.currencies['gold']/cost)
            for amount in range(amount):
                options.append(amount)
            #players choice
            choice = player_input("How many iron ingots would you like to purchase?",options,"shop", f"Total Gold: {game.player.inventory.currencies['gold']}\nEach iron ingot costs 2 gold pieces. You have enough gold for {amount}.")
            
            #cost of chosen number
            cost = choice * 2
            game.player.inventory.resources['iron ingot'] += choice
            game.player.inventory.currencies['gold'] -= (choice * cost)

            os.system("cls")

            print(f"You have purchased {choice} iron ingots for {cost} golden coins. Your total iron ingots is now {game.player.inventory.resources['iron ingot']}")
            print("")
            print(input("Press Enter to continue..."))
            os.system("cls")
    #meals
        if choice == 2:
            cost = 2
            options = []
            amount = int(game.player.inventory.currencies['gold']/cost)
            for amount in range(amount):
                options.append(amount)
            #players choice
            choice = player_input("How many meals would you like to purchase?",options,"shop", f"Total Gold: {game.player.inventory.currencies['gold']}\nEach meal costs 2 gold pieces. You have enough gold for {amount}.")
            
            #cost of chosen number
            cost = choice * 2
            game.player.inventory.resources['meals'] += choice
            game.player.inventory.currencies['gold'] -= (choice * cost)

            os.system("cls")

            print(f"You have purchased {choice} meals for {cost} golden coins. Your total meals is now {game.player.inventory.resources['meals']}")
            print("")
            print(input("Press Enter to continue..."))
            os.system("cls")
    #weapons
        elif choice == 3:
            while True:
                options = range(len(game.player.inventory.weapons)+1)
                
                #if no weapons
                if len(game.player.inventory.weapons) == 0:
                    print("You have no weapons!")
                    wait_for_enter()
                    return
                weapon_list = []
                print(f"You currently have {len(game.player.inventory.weapons)} weapons!")
                number_of_weapon = 0
                for weapon in game.player.inventory.weapons:
                    #print(f"{number_of_weapon}. {weapon.quality} {weapon.name} is worth {weapon.value} and does {weapon.damage} damage.")
                    weapon_list.append(weapon)
                    number_of_weapon += 1
                print()

                choice = player_input("Please select which weapon you want to sell",weapon_list,"weapons")
        

                if choice == len(weapon_list) - 1:
                    return

                os.system("cls")
                print(choice)
                print(weapon_list)
                if game.player.inventory.weapons[int(choice)] == game.player.main_hand:
                    print("You can't sell this while it's your current mainhand weapon!")
                    print(input("Press Enter to continue..."))
                    os.system("cls")
                    return

                print(f"You have selected {game.player.inventory.weapons[int(choice)].quality} {game.player.inventory.weapons[int(choice)].name} that does {game.player.inventory.weapons[int(choice)].damage} and is worth {game.player.inventory.weapons[int(choice)].value} to sell")
                game.player.inventory.currencies['gold'] += game.player.inventory.weapons[int(choice)].value
                game.player.inventory.weapons.pop(choice)
                print(f"You now have {game.player.inventory.currencies['gold']} gold")
                print(input("Press Enter to continue..."))
                os.system("cls")
                return

        elif choice == "4":
            os.system("cls")
          
def inventory():
    while True:
        specific_input = ["1", "2", "3", "4", "5"]
        print("1. Iron Ingots")
        print("2. Meals")
        print("3. Gold")
        print("4. Weapons")
        print("5. Back")
        print("")
        choice = input("What would you like to check?")
        os.system("cls")
        
        if choice not in specific_input:

            print("1. Iron Ingots")
            print("2. Meals")
            print("3. Gold")
            print("4. Weapons")
            print("5. Back")
            print("")
            choice = input("What would you like to check?")
            os.system("cls")

        if choice == "1":
            os.system("cls")
            print(f"You currently have {game.player.inventory.resources['iron ingot']} iron ingots!")
            print("")
            print(input("Press Enter to continue..."))
            os.system("cls")

        elif choice == "2":
            os.system("cls")
            print(f"You currently have {game.player.inventory.resources['meal']} meals!")
            print("")
            print(input("Press Enter to continue..."))
            os.system("cls")

        elif choice == "3":
            os.system("cls")
            print(f"You currently have {game.player.inventory.currencies['gold']} gold coins!")
            print("")
            print(input("Press Enter to continue..."))
            os.system("cls")


        elif choice == "4":

            while True:
                specific_input = ["1", "2"]
                os.system("cls")
                print(f"You currently have {len(game.player.inventory.weapons)} weapons and your current mainhand is {game.player.main_hand.quality} {game.player.main_hand.name} that does {game.player.main_hand.damage} damage!")
                number_of_weapon = 1
                for weapon in game.player.inventory.weapons:
                    print(f"{number_of_weapon}. {weapon.quality} {weapon.name} is worth {weapon.value} and does {weapon.damage} damage.")
                    number_of_weapon += 1
                print()
                print("1. Change mainhand")
                print("2. back")
                print()
                choice = input("What would you like to check?")
                os.system("cls")

                if choice not in specific_input:

                    os.system("cls")
                    print(f"You currently have {len(game.player.inventory.weapons)} weapons and your current mainhand is {game.player.main_hand.quality} {game.player.main_hand.name} that does {game.player.main_hand.damage} damage!")
                    number_of_weapon = 1
                    for weapon in game.player.inventory.weapons:
                        print(f"{number_of_weapon}. {weapon.quality} {weapon.name} is worth {weapon.value} and does {weapon.damage} damage.")
                        number_of_weapon += 1
                    print()
                    print("1. Change mainhand")
                    print("2. back")
                    print()
                    choice = input("What would you like to check?")
                    os.system("cls")

                if choice == "1":

                    while True:
                        specific_input = range(len(game.player.inventory.weapons)+1)

                        if len(game.player.inventory.weapons) == 0:
                            print("You have no weapons!")
                            print(input("Press Enter to continue..."))
                            os.system("cls")
                            return

                        print(f"You currently have {len(game.player.inventory.weapons)} weapons and your current mainhand is {game.player.main_hand.quality} {game.player.main_hand.name} that does {game.player.main_hand.damage} damage!!")
                        number_of_weapon = 1
                        for weapon in game.player.inventory.weapons:
                            print(f"{number_of_weapon}. {weapon.quality} {weapon.name} is worth {weapon.value} and does {weapon.damage} damage.")
                            number_of_weapon += 1
                        print()
                        try:
                            choice = int(input("Please select which weapon you want as your mainhand:"))
                        except:
                            os.system("cls")
                            print("Invalid Input: Returning to main menu to prevent program crash...")
                            print(input("Press Enter to continue..."))
                            os.system("cls")
                            return
                        
                        os.system("cls")

                        if choice not in specific_input:
                            
                            print(f"You currently have {len(game.player.inventory.weapons)} weapons and your current mainhand is {game.player.main_hand.quality} {game.player.main_hand.name} that does {game.player.main_hand.damage} damage!!")
                            number_of_weapon = 1
                            for weapon in game.player.inventory.weapons:
                                print(f"{number_of_weapon}. {weapon.quality} {weapon.name} is worth {weapon.value} and does {weapon.damage} damage.")
                                number_of_weapon += 1
                            print()
                            choice = input("Please select which weapon you want as your mainhand:")
                            os.system("cls")
                        os.system("cls")
                        choice -= 1
                        print(f"You have selected {game.player.inventory.weapons[int(choice)].quality} {game.player.inventory.weapons[int(choice)].name} that does {game.player.inventory.weapons[int(choice)].damage} damage as your mainhand.")
                        game.player.main_hand = game.player.inventory.weapons[int(choice)]
                        print(input("Press Enter to continue..."))
                        os.system("cls")
                        return
                if choice == "2":
                    return





        elif choice == "5":
            break
            os.system("cls")

def set_dead(self):
    self.health = 0

def dead():
    print("GAME OVER")
    print(f"{game.player.name} survived {game.player.days_survived} days!")
    wait_for_enter()
    return    

def sleep():
    meals = game.player.inventory.resources['meal']
    days_survived = game.player.days_survived
    action_left = game.player.actions_left
    hunger = game.player.hunger
    dead_chance = random.randint(1, 25)
    if dead_chance != 1:
        print("After a long day, you enter your bedroom to go to bed.")
        time.sleep(2)
        if meals > 0:
            meals -= 1
            print(f"Before going to bed you decide to have a meal. Your hunger has been restored! You now have a total of {meals} meals")
            time.sleep(2)
            print("You made it through the night!")
            print("")
            print(input("Press Enter to continue..."))
            os.system("cls")
            game.player.actions_left = 3
            days_survived += 1
            hunger = 0
        elif meals == 0 and hunger == 1:
            print("Before going to bed you decided to have a meal, but you have none again! You enter a berzerk frenzy until one of the towns guards restrains you.")
            print("Sadly, this is where your story ends. You will spend the last of your hungry existance behind bars.")
            print(input("Press Enter to continue..."))
            os.system("cls")
            dead()
            
        elif meals == 0:
            print("Before going to bed you decided to have a meal, but you have none! You decide to go to bed hungry...")
            time.sleep(2)
            print("You made it through the night!")
            print("")
            print(input("Press Enter to continue..."))
            os.system("cls")
            game.player.actions_left = 3
            days_survived += 1
            game.player.hunger += 1

    else:
        print("You wake up to the sound of wood creaking...")
        time.sleep(1)
        print("By the time you realize you also hear footsteps, it's too late...")
        time.sleep(2)
        print("You exhale your last breath as the masked man drives a sword into your chest.")
        print("")
        dead()

class Weapon:
    def __init__(self, name, value, quality, damage, speed):
        self.name = name
        self.value = value
        self.quality = quality
        self.damage = damage
        self.speed = speed

    def craft_weapon():
        weapon_type = random.choice(["Sword", "Axe", "Dagger", "Mace"])
        if weapon_type == "Dagger":
            base_damage = 3
            speed = 1
        elif weapon_type == "Sword":
            base_damage = 4
            speed = 2
        elif weapon_type == "Axe":
            base_damage = 5
            speed = 3
        elif weapon_type == "Mace":
            base_damage = 6
            speed = 4

        quality = random.choice(["Poor", "Normal", "Good", "Great", "Perfect"])
        if quality == "Poor":
            quality_damage = random.randint(1,1)
        elif quality == "Normal":
            quality_damage = random.randint(1,2)
        elif quality == "Good":
            quality_damage = random.randint(2,2)
        elif quality == "Great":
            quality_damage = random.randint(2,3)
        elif quality == "Perfect":
            quality_damage = random.randint(3,3)
            speed -= 1

        damage = base_damage + quality_damage
        value = base_damage + quality_damage
        weapon = Weapon(weapon_type, value, quality, damage, speed)

        return weapon

def dungeon(player):

    #check if player has enough actions left for the day
    if game.player.actions_left < 3:
        print("As much as you'd like to go dungeon crawling, you fear you're too tired!")
        print("Maybe try again tomorrow...")
        print(input("Press Enter to continue..."))
        os.system("cls")
        return

    #assigning some variables that will be used later + setting up dungeon loot table
    game.player.actions_left -= 2
    dungeon_loot_table = []
    number_of_enemies = range(3)


    print("You decided to venture out to an old cave you seldom heard stories about...")
    print("But the stories you have heard make you believe many don't live to tell the tale...")
    print(input("Press Enter to continue..."))
    os.system("cls")


    print("Upon arriving to the cave, it's everything you imagined...")
    print("There is the faint smell of death and the occasional blood trail as you step into the darkness. Luckily, you brought your torch!")
    print(input("Press Enter to continue..."))
    os.system("cls")

    print("Get to the good stuff. Fighting time!")
    print(input("Press Enter to continue..."))
    os.system("cls")
    #counts raiders

    for enemy in number_of_enemies:
        #creates enemy 
        game.enemy_maker("enemy")
        print("You enter combat!")
        #Sends game to combat state
        combat()
        if is_Target_dead(game.player):
            return
        dungeon_loot_table.append(game.current_enemy.inventory.weapons[0])

    if is_Target_dead(game.player):
        return

    print("You did it!")
    print(input("Press Enter to continue..."))
    os.system("cls")
    
    counter = 1
    print("The following items have been added to your inventory:")
    print()
    for item in dungeon_loot_table:
        print(f"{counter}. {item.quality} {item.name} that does {item.damage} damage and is worth {item.value}")
        game.player.inventory.add_weapon(item)
        counter += 1
    print()
    print(input("Press Enter to continue..."))
    os.system("cls")

    print("After reaping your rewards, you begin walking for the exit. Suddenly, you realize how tired you are.")
    print(input("Press Enter to continue..."))
    os.system("cls")

    print("The walk back was uneventful, but you've never been more happy to see the large gates of the city. Behind which, you call home.")
    print(input("Press Enter to continue..."))
    os.system("cls")
 
class Game():

    startup_values = onStartup()
    player = Character(startup_values[0])
    player.set_profession(startup_values[1])
    player.inventory.add_weapon(Weapon.craft_weapon())
    player.main_hand = player.inventory.weapons[0]
    player.health = 25
    current_enemy = None

    def enemy_maker(self, enemy_name):
        enemy_character = Character(enemy_name)
        enemy_character.inventory.add_weapon(Weapon.craft_weapon())
        enemy_character.main_hand = enemy_character.inventory.weapons[0]
        self.current_enemy = enemy_character

    def daily_work(player):
        global professions
        random_int = random.randint(1,3)
        if player.profession == "Woodcutter":
            if random_int == 1:
                earned_daily = random.randint(1,3)
                player.actions_left -= 1
                print("You went to the local log-yard and helped the locals split some wood.")
                print(f"Although easy, they paid you {earned_daily} gold coins")
                player.inventory.add_currency('gold', earned_daily)
                print(f"You now have {player.inventory.currencies['gold']} gold coins!")
                print()
                print(input("Press Enter to continue..."))
                os.system("cls")
                return earned_daily

            elif random_int == 2:
                earned_daily = random.randint(2,5)
                player.actions_left -= 1
                print("Your neighbor told you about a funny looking tree he found on his walk.")
                print("You decide to go chop it down. Using your mule and cart, you bring it to the local carpenter.")
                print(f"He pays you {earned_daily} for the rare tree!")
                player.inventory.add_currency('gold', earned_daily)
                print(f"You now have {player.inventory.currencies['gold']} gold coins!")
                print()
                print(input("Press Enter to continue..."))
                os.system("cls")
                return earned_daily

            elif random_int == 3:
                earned_daily = random.randint(1,3)
                player.actions_left -= 1
                print("You went to your usual spot for chopping down large oak trees.")
                print("As expected, your local carpenter was happy to see you brining him more product.")
                print(f"For a few hours work, he paid you {earned_daily} gold coins")
                player.inventory.add_currency('gold', earned_daily)
                print(f"You now have {player.inventory.currencies['gold']} gold coins!")
                print()
                print(input("Press Enter to continue..."))
                os.system("cls")
                return earned_daily

        elif player.profession == "Miner":
            if random_int == 1:
                earned_daily = random.randint(1,3)
                player.actions_left -= 1
                print("You went to the local coal mine and helped the locals mine some coal.")
                print(f"Although easy, they paid you {earned_daily} gold coins")
                player.inventory.add_currency('gold', earned_daily)
                print(f"You now have {player.inventory.currencies['gold']} gold coins!")
                print()
                print(input("Press Enter to continue..."))
                os.system("cls")
                return earned_daily

            elif random_int == 2:
                earned_daily = random.randint(2,5)
                player.actions_left -= 1
                print("Your neighbor told you about a funny looking rock he found on his walk.")
                print("You decide to go mine it. Using your mule and cart, you bring it to the local jeweler.")
                print(f"He pays you {earned_daily} for the rare rock!")
                player.inventory.add_currency('gold', earned_daily)
                print(f"You now have {player.inventory.currencies['gold']} gold coins!")
                print()
                print(input("Press Enter to continue..."))
                os.system("cls")
                return earned_daily

            elif random_int == 3:
                earned_daily = random.randint(1,3)
                player.actions_left -= 1
                print("You went to your usual spot for mining raw iron.")
                print("As expected, your local whitesmith was happy to see you brining him more product.")
                print(f"For a few hours work, he paid you {earned_daily} gold coins")
                player.inventory.add_currency('gold', earned_daily)
                print(f"You now have {player.inventory.currencies['gold']} gold coins!")
                print()
                print(input("Press Enter to continue..."))
                os.system("cls")
                return earned_daily
                
        elif player.profession == "Fisherman":
            if random_int == 1:
                earned_daily = random.randint(1,3)
                player.actions_left -= 1
                print("You went to the local river and helped the locals netfish for river trout.")
                print(f"Although easy, they paid you {earned_daily} gold coins")
                player.inventory.add_currency('gold', earned_daily)
                print(f"You now have {player.inventory.currencies['gold']} gold coins!")
                print()
                print(input("Press Enter to continue..."))
                os.system("cls")
                return earned_daily

            elif random_int == 2:
                earned_daily = random.randint(2,5)
                player.actions_left -= 1
                print("Your neighbor told you about a funny looking fish swimming around in a pond nearby.")
                print("You decide to go catch it. You bring it to the local chef.")
                print(f"He pays you {earned_daily} for the rare fish!")
                player.inventory.add_currency('gold', earned_daily)
                print(f"You now have {player.inventory.currencies['gold']} gold coins!")
                print()
                print(input("Press Enter to continue..."))
                os.system("cls")
                return earned_daily

            elif random_int == 3:
                earned_daily = random.randint(1,3)
                player.actions_left -= 1
                print("You went to your usual spot for fishing.")
                print("As expected, your local chef was happy to see you brining him more product.")
                print(f"For a few hours work, he paid you {earned_daily} gold coins")
                player.inventory.add_currency('gold', earned_daily)
                print(f"You now have {player.inventory.currencies['gold']} gold coins!")
                print()
                print(input("Press Enter to continue..."))
                os.system("cls")
                return earned_daily
        
        elif player.profession == "Herbalist":
            if random_int == 1:
                earned_daily = random.randint(1,3)
                player.actions_left -= 1
                print("You went to the local apple orchard and helped the locals pick apples.")
                print(f"Although easy, they paid you {earned_daily} gold coins")
                player.inventory.add_currency('gold', earned_daily)
                print(f"You now have {player.inventory.currencies['gold']} gold coins!")
                print()
                print(input("Press Enter to continue..."))
                os.system("cls")
                return earned_daily

            elif random_int == 2:
                earned_daily = random.randint(2,5)
                player.actions_left -= 1
                print("Your neighbor told you about a funny looking plant he saw while on his walk.")
                print("You decide to go pick every berry off it. You bring it to the local chef.")
                print(f"He pays you {earned_daily} for the rare fish!")
                player.inventory.add_currency('gold', earned_daily)
                print(f"You now have {player.inventory.currencies['gold']} gold coins!")
                print()
                print(input("Press Enter to continue..."))
                os.system("cls")
                return earned_daily

            elif random_int == 3:
                earned_daily = random.randint(1,3)
                player.actions_left -= 1
                print("You went to your usual spot for picking strawberries.")
                print("As expected, your local chef was happy to see you brining him more product.")
                print(f"For a few hours work, he paid you {earned_daily} gold coins")
                player.inventory.add_currency('gold', earned_daily)
                print(f"You now have {player.inventory.currencies['gold']} gold coins!")
                print()
                print(input("Press Enter to continue..."))
                os.system("cls")
                return earned_daily  
           
def combat():
    #grab both mainhand speeds
    enemy_speed = game.current_enemy.main_hand.speed
    player_speed = game.player.main_hand.speed

    if enemy_speed > player_speed:
        faster = game.current_enemy
        slower = game.player
    else:
        faster = game.player
        slower = game.current_enemy

    while True:
        #fighting begins
        print(f"{faster.name} attacks first, since they have a faster weapon. They deal {faster.main_hand.damage} points of damage!")
        slower.health -= faster.main_hand.damage

        #Is player or enemy dead after faster attack?
        if is_Target_dead(game.current_enemy):
            print("After that blow, the enemy falls to the ground...")
            print(f"Your current health is {game.player.health} but is being refilled to full for the next fight (Beta Feature).")
            game.player.health = 15
            print(input("Press Enter to continue..."))
            os.system("cls")
            return
        elif is_Target_dead(game.player):
            print("The enemy gets the best of you...")
            wait_for_enter()
            return

        #Slower didn't die, he may attack
        print(f"In retaliation, {slower.name} attacks and deals {slower.main_hand.damage} points of damage")
        print()
        print(input("Press Enter to continue..."))
        os.system("cls")

        #calculating health
        faster.health -= slower.main_hand.damage
        #checking to see slower died
        if is_Target_dead(game.current_enemy):
            print("After that blow, the enemy falls to the ground...")
            print(f"Your current health is {game.player.health} but is being refilled to full for the next fight (Beta Feature).")
            print(input("Press Enter to continue..."))
            game.player.health = 15
            os.system("cls")
            return

        elif is_Target_dead(game.player):
            print("The enemy gets the best of you...")
            wait_for_enter()
            return

        options = [
            "Attack",
            "Run Away"
        ]

        choice = player_input("What would you like to do?", options, "int",f"Enemy health: {game.current_enemy.health}\nYour health: {game.player.health}\n")

        os.system("cls")
            
        if choice == 1:
            continue

        if choice == 2:
            print("You sprint away for the entrance to the cave. You hear a mocking laugh as you exit...")
            return

game = Game()

while game.player.health > 0:
    if game.player.actions_left <= 0:
        sleep()

    print("1. Work")
    print("2. Craft Item")
    print("3. Shop")
    print("4. Check Inventory")
    print("5. Dungeon Time!")
    print("")

    choice = input("What would you like to do?")

    os.system("cls")

    if choice == "1":
        Game.daily_work(game.player)

    if choice == "2":
        crafting(game.player)

    if choice =="3":
        shop()
                
    if choice =="4":
        inventory()

    if choice =="5":
        dungeon(game.player)
os.system("cls")
dead()


