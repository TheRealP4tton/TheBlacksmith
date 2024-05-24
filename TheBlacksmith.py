import random
import time
import os

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
        self.resources = {'meal': 0, 'iron ingot': 0}
        self.currencies = {'gold':0}
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

def onStartup():
    global professions

    print(" ____  _            _                  _ _   _     ")
    print("| __ )| | __ _  ___| | _____ _ __ ___ (_) |_| |__  ")
    print("|  _ \| |/ _` |/ __| |/ / __| '_ ` _ \| | __| '_ \ ")
    print("| |_) | | (_| | (__|   <\__ \ | | | | | | |_| | | |")
    print("|____/|_|\__,_|\___|_|\_\___/_| |_| |_|_|\__|_| |_|")
    print()
    print(input("Press Enter to continue..."))
    os.system("cls")

    print("You will live the simple life of a blacksmith.")
    print("Work, craft items, and sell them to make money needed to survive.")
    print(input("Press Enter to continue..."))
    os.system("cls")

    print("Before you begin, we need to figure out who you are!")
    print(input("Press Enter to continue..."))
    os.system("cls")

    player = input("What would you like to be called?")
    os.system("cls")

    while True:
        if player == "":
            print("Sadly you cannot be nameless. How fun would that be?")
            print(input("Press Enter to continue..."))
            os.system("cls")

            player = input("What would you like to be called?")
            os.system("cls")

        else:
            break

    print(f"Its been decided, you will be called {player} from here on out!")
    print(input("Press Enter to continue..."))
    os.system("cls")

    print("Besides just being a blacksmith, you also have the chance to choose a second profession.")
    print("What will you choose?")
    print(input("Press Enter to continue..."))
    os.system("cls")

    print("Please choose a secondary profession:")
    print("1. Woodcutter")
    print("2. Miner")
    print("3. Fisherman")
    print("4. Herbalist")
    profession_number = input("Which will you choose? ")
    os.system("cls")
    professions = ["Woodcutter", "Miner", "Fisherman", "Herbalist"]
    while True:
        if profession_number == str(profession_number) == "" or int(profession_number) < 0 or int(profession_number) > (len(professions)):

            print("That is not an option.")
            print(input("Press Enter to continue..."))
            os.system("cls")

            print("Please choose a secondary profession:")
            print("1. Woodcutter")
            print("2. Miner")
            print("3. Fisherman")
            print("4. Herbalist")
            profession_number = input("Which will you choose? ")
            os.system("cls")

        else:
            break
    
    player_profession = professions[(int(profession_number)-1)]

    print(f"So you've chosen to be a {player_profession}, good choice!")
    print(input("Press Enter to continue..."))
    os.system("cls")

    print(f"Let the story of {player} the Blacksmith unfold")
    print("Try to survive as long as you can.")
    print(input("Press Enter to continue..."))
    os.system("cls")
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
        print(input("Press Enter to continue..."))
        os.system("cls")
        return
        

    print("You decided to craft an item of unknown quality...")
    print(f"After many hours, you manage to craft a {newly_crafted.quality} {newly_crafted.name} that does {newly_crafted.damage} damage worth {newly_crafted.value} gold coins!")
    print(f"You used {ingots_used} in the process")
    print()
    print(f"Would you like to sell it for {newly_crafted.value} or add it to your inventory?")
    print("1. Sell")
    print("2. Keep")
    print()
    choice = input("What would you like to do?")
    os.system("cls")

    while True:

        specific_input = ["1", "2"]

        if choice not in specific_input:
                print("You decided to craft an item of unknown quality...")
                print(f"After many hours, you manage to craft a {newly_crafted.quality} {newly_crafted.name} that does {newly_crafted.damage} damage worth {newly_crafted.value} gold coins!")
                print(f"You used {ingots_used} in the process")
                print()
                print(f"Would you like to sell it for {newly_crafted.value} or add it to your inventory?")
                print("1. Sell")
                print("2. Keep")
                print()
                choice = input("What would you like to do?")
                os.system("cls")

        if choice == "1":
            print(f"You sold the {newly_crafted.quality} {newly_crafted.name} for {newly_crafted.value} gold pieces.")
            game.player.inventory.add_currency('gold', newly_crafted.value)
            game.player.inventory.resources['iron ingot'] -= ingots_used
            print(f"You now have {game.player.inventory.currencies['gold']} gold coins!")
            print()
            print(input("Press Enter to continue..."))
            os.system("cls")
            break
    
        elif choice == "2":
            print(f"You decided the keep the {newly_crafted.quality} {newly_crafted.name}.")
            game.player.inventory.add_weapon(newly_crafted)
            game.player.inventory.resources['iron ingot'] -= ingots_used
            print(f"You now have {len(game.player.inventory.weapons)} weapons in your inventory")
            game.player.main_hand = newly_crafted
            print(input("Press Enter to continue..."))
            os.system("cls")
            break

def shop():



    while True:
        print("Welcome to the store! Spend your hard earned currency here!")
        print(f"You currently have {game.player.inventory.currencies['gold']} to spend:")
        print("")
        print("1. Buy iron ingot | $2 / each")
        print("2. Buy meal       | $2 / each")
        print("3. Sell Weapons")
        print("4. Back")
        print("")
        choice = input("What would you like to do?")
        os.system("cls")

        if choice == "1":
            choice = input(f"How many iron ingots would you like to purchase? (0 - {int(game.player.inventory.currencies['gold']/2)})")
            int_choice = choice


            while True:
                try:
                    int_choice = int(choice)
                    break 
                except:
                    print("That is not an option.")
                    print(input("Press Enter to continue..."))
                    os.system("cls")
                    choice = input(f"How many iron ingots would you like to purchase? (0 - {int(game.player.inventory.currencies['gold']/2)})")
            
            cost = int_choice * 2
            if choice == "0":
                print()
                os.system("cls")
            elif game.player.inventory.currencies['gold'] >= cost:
                game.player.inventory.resources['iron ingot'] += int_choice
                game.player.inventory.currencies['gold'] -= (int_choice * 2)
                os.system("cls")
                print(f"You have purchased {choice} iron ingots. Your total iron ingots is now {game.player.inventory.resources['iron ingot']}")
                print("")
                print(input("Press Enter to continue..."))
                os.system("cls")
            else:
                print("You don't seem to have enough currency for that!")
                print("")
                print(input("Press Enter to continue..."))
                os.system("cls")

        elif choice == "2":
            choice = input(f"How many meals would you like to purchase? (0 - {int(game.player.inventory.currencies['gold']/2)})")
            int_choice = int(choice)
            cost = int_choice * 2
            if choice == "0":
                print()
                os.system("cls")
            elif game.player.inventory.currencies['gold'] >= cost:
                game.player.inventory.resources['meal'] += int_choice
                game.player.inventory.currencies['gold'] -= (int_choice * 2)
                os.system("cls")
                print(f"You have purchased {choice} meals. Your total meals is now {game.player.inventory.resources['meal']}")
                print("")
                print(input("Press Enter to continue..."))
                os.system("cls")
            else:
                print("You don't seem to have enough currency for that!")
                print("")
                print(input("Press Enter to continue..."))
                os.system("cls")

        elif choice == "3":
            while True:
                specific_input = range(len(game.player.inventory.weapons)+1)

                if len(game.player.inventory.weapons) == 0:
                    print("You have no weapons!")
                    print(input("Press Enter to continue..."))
                    os.system("cls")
                    return

                print(f"You currently have {len(game.player.inventory.weapons)} weapons!")
                number_of_weapon = 1
                for weapon in game.player.inventory.weapons:
                    print(f"{number_of_weapon}. {weapon.quality} {weapon.name} is worth {weapon.value} and does {weapon.damage} damage.")
                    number_of_weapon += 1
                print()
                try:
                    choice = int(input("Please select which weapon you want to sell:"))
                except:
                    os.system("cls")
                    print("Invalid Input: Returning to main menu to prevent program crash...")
                    print(input("Press Enter to continue..."))
                    os.system("cls")
                    return

                os.system("cls")

                if choice not in specific_input:
                    
                    print(f"You currently have {len(game.player.inventory.weapons)} weapons!")
                    number_of_weapon = 1
                    for weapon in game.player.inventory.weapons:
                        print(f"{number_of_weapon}. {weapon.quality} {weapon.name} is worth {weapon.value} and does {weapon.damage} damage.")
                        number_of_weapon += 1
                    print()
                    choice = input("Please select which weapon you want to sell:")
                    os.system("cls")
                    
                os.system("cls")
                choice -= 1
                
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
            break

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

def dead():
    game.player.health = 0
    print("GAME OVER")
    print(f"{game.player.name} survived {game.player.days_survived} days!")
    print(input("Press Enter to continue..."))

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

class Game():

    startup_values = onStartup()
    player = Character(startup_values[0])
    player.set_profession(startup_values[1])
    starter_weapon = Weapon.craft_weapon()
    player.inventory.add_weapon(starter_weapon)
    player.main_hand = player.inventory.weapons[0]
    player.health = 15

    def enemy_maker(enemy_name):
        enemy_name = Character(enemy_name)

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
        

def dungeon(player):
    game.player.actions_left -= 2

    dungeon_loot_table = []
    number_of_enemies = range(random.randint(1,3))


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
    number = 1

    for enemy in number_of_enemies:
        current_enemy = Character(enemy)
        enemy_weapon = Weapon.craft_weapon()
        current_enemy.inventory.add_weapon(enemy_weapon)
        current_enemy.main_hand = current_enemy.inventory.weapons[0]
        print(f"You are being attacked by raider number {number}! A raider holding a {current_enemy.main_hand.quality} {current_enemy.main_hand.name} runs at you! You prepare yourself as the battle stars...")
        specific_input = ["1", "2"]
        while True:
            damage = game.player.main_hand.damage
            enemy_damage = current_enemy.main_hand.damage
            print(f"Enemy health: {current_enemy.health}")
            print(f"Your health: {game.player.health}")
            print("")
            print("1. Attack")
            print("2. Run away")
            choice = input("What would you like to do?")
            os.system("cls")

            if choice not in specific_input:
                print(f"Enemy health: {current_enemy.health}")
                print(f"Your health: {game.player.health}")
                print("")
                print("1. Attack")
                print("2. Run away")
                choice = input("What would you like to do?")
                os.system("cls")
            
            if choice == "1":

                    #if player has faster weapon:
                if game.player.main_hand.speed < current_enemy.main_hand.speed:

                    print("You have the faster weapon, you attack first!")
                    print(f"You swing your {game.player.main_hand.name} and deal {damage} points of damage!")
                    current_enemy.health -= damage
                    print(input("Press Enter to continue..."))
                    os.system("cls")
                    
                    if current_enemy.health <= 0:
                        print("After that blow, the enemy falls to the ground...")
                        print(f"Your current health is {game.player.health} but is being refilled to full for the next fight (Beta Feature).")
                        #
                        game.player.health = 15
                        print(f"New health value: {game.player.health}")
                        dungeon_loot_table.append(current_enemy.inventory.weapons[0])
                        number += 1
                        print(input("Press Enter to continue..."))
                        os.system("cls")
                        break

                    else:
                        
                        print(f"The raider counter-attacks and deals {enemy_damage} points of damage.")
                        player.health -= enemy_damage
                        print(input("Press Enter to continue..."))
                        os.system("cls")

                        if player.health <= 0:
                            os.system("cls")
                            print("Oh no! Your health has fallen to 0...")
                            print(input("Press Enter to continue..."))
                            os.system("cls")
                            return
                            dead()
                        
            
                    #if enemy has faster weapon:
                else: 
                    print("The raider has the faster weapon, he attacks first!")
                    print(f"The raider attacks you and deals {enemy_damage} points of damage.")
                    player.health -= enemy_damage
                    print(input("Press Enter to continue..."))
                    os.system("cls")

                    if player.health <= 0:
                            os.system("cls")
                            print("Oh no! Your health has fallen to 0...")
                            print(input("Press Enter to continue..."))
                            os.system("cls")
                            return
                            dead()
                    
                    print(f"You swing your {game.player.main_hand.name} and deal {damage} points of damage!")
                    current_enemy.health -= damage
                    print(input("Press Enter to continue..."))
                    os.system("cls")
                    
                    if current_enemy.health <= 0:
                        print("After that blow, the enemy falls to the ground...")
                        print(f"Your current health is {game.player.health} but is being refilled to full for the next fight.")
                       
                        game.player.health = 15
                        print(f"New health value: {game.player.health}")
                        dungeon_loot_table.append(current_enemy.inventory.weapons[0])
                        number += 1
                        print(input("Press Enter to continue..."))
                        os.system("cls")
                        break


            if choice == "2":
                print("You sprint away for the entrance to the cave. You hear a mocking laugh as you exit...")
                return
    print("You did it!")
    print(input("Press Enter to continue..."))
    os.system("cls")
    
    counter = 1
    print("The following items have been added to your inventory:")
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

dead()


