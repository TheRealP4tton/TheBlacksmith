import random
import time
import os

isdead = False
money = 100
action_left = 3
days_survived = 0
iron_ingots = 10
meals = 0
hunger = 0
crafted_item = []
chosen_job = ""
char_name = ""
professions = ["Woodcutter", "Miner", "Fisherman", "Herbalist"]

def onStartup():
    global char_name
    global chosen_job
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

    char_name = input("What would you like to be called?")
    os.system("cls")

    while True:
        if char_name == "":
            print("Sadly you cannot be nameless. How fun would that be?")
            print(input("Press Enter to continue..."))
            os.system("cls")

            char_name = input("What would you like to be called?")
            os.system("cls")

        else:
            break

    print(f"Its been decided, you will be called {char_name} from here on out!")
    print(input("Press Enter to continue..."))
    os.system("cls")

    print(f"Besides just being a blacksmith, you also have the chance to choose a second profession.")
    print(f"What will you choose?")
    print(input("Press Enter to continue..."))
    os.system("cls")

    print(f"Please choose a secondary profession:")
    print(f"1. Woodcutter")
    print(f"2. Miner")
    print(f"3. Fisherman")
    print(f"4. Herbalist")
    user_input = int(input("Which will you choose? "))
    os.system("cls")

    chosen_job = professions[(user_input-1)]

    print(f"So you've chosen to be a {chosen_job}, good choice!")
    print(input("Press Enter to continue..."))
    os.system("cls")

    print(f"Let the story of {char_name} the Blacksmith unfold")
    print(f"Try to survive as long as you can.")
    print(input("Press Enter to continue..."))
    os.system("cls")

def daily_work():
    global money
    global action_left
    global chosen_job
    global char_name
    global professions
    random_int = random.randint(1,3)

    if chosen_job == professions[0]:
        if random_int == 1:
            earned_daily = random.randint(1,3)
            action_left -= 1
            print(f"You went to the local log-yard and helped the locals split some wood.")
            print(f"Although easy, they paid you {earned_daily} silver coins")
            money += earned_daily
            print(f"You now have {money} silver coins!")
            print()
            print(input("Press Enter to continue..."))
            os.system("cls")

        elif random_int == 2:
            earned_daily = random.randint(2,5)
            action_left -= 1
            print(f"Your neighbor told you about a funny looking tree he found on his walk.")
            print(f"You decide to go chop it down. Using your mule and cart, you bring it to the local carpenter.")
            print(f"He pays you {earned_daily} for the rare tree!")
            money += earned_daily
            print(f"You now have {money} silver coins!")
            print()
            print(input("Press Enter to continue..."))
            os.system("cls")
        elif random_int == 3:
            earned_daily = random.randint(1,3)
            action_left -= 1
            print(f"You went to your usual spot for chopping down large oak trees.")
            print(f"As expected, your local carpenter was happy to see you brining him more product.")
            print(f"For a few hours work, he paid you {earned_daily} silver coins")
            money += earned_daily
            print(f"You now have {money} silver coins!")
            print()
            print(input("Press Enter to continue..."))
            os.system("cls")

    elif chosen_job == professions[1]:
        if random_int == 1:
            earned_daily = random.randint(1,3)
            action_left -= 1
            print(f"You travel to your local coal deposit and gather some coal out of the mine.")
            print(f"The local tavern was more than happy to take the coal off of your hands.")
            print(f"The tavern paid you {earned_daily} silver coins")
            money += earned_daily
            print(f"You now have {money} silver coins!")
            print()
            print(input("Press Enter to continue..."))
            os.system("cls")
        elif random_int == 2:
            earned_daily = random.randint(2,5)
            action_left -= 1
            print(f"Your neighbor told you about a funny looking rock he found on his walk.")
            print(f"You decide to go split it in half. Using your mule and cart, you bring back shiny rocks.")
            print(f"Your local jewler was intriqued by the rocks and said he would buy them.")
            print(f"He pays you {earned_daily} for the shiny rocks!")
            money += earned_daily
            print(f"You now have {money} silver coins!")
            print()
            print(input("Press Enter to continue..."))
            os.system("cls")
        elif random_int == 3:
            earned_daily = random.randint(1,3)
            action_left -= 1
            print(f"You went to your usual spot for mining iron ore.")
            print(f"As expected, your local whitesmith was exicted to have more product")
            print(f"For a few hours work, he paid you {earned_daily} silver coins")
            money += earned_daily
            print(f"You now have {money} silver coins!")
            print()
            print(input("Press Enter to continue..."))
            os.system("cls")

    elif chosen_job == professions[2]:
        if random_int == 1:
            earned_daily = random.randint(1,3)
            action_left -= 1
            print(f"You travel to your stream to catch some trout.")
            print(f"The local tavern was more than happy to take the fish off of your hands.")
            print(f"The tavern paid you {earned_daily} silver coins")
            money += earned_daily
            print(f"You now have {money} silver coins!")
            print()
            print(input("Press Enter to continue..."))
            os.system("cls")
        elif random_int == 2:
            earned_daily = random.randint(2,5)
            action_left -= 1
            print(f"Your neighbor told you about a funny looking fish he saw in a pond near by.")
            print(f"You decide to go catch the fish.")
            print(f"A strange man stopped you on your way back and said he'd take the fish off your hands.")
            print(f"He pays you {earned_daily} for the funny looking fish!")
            money += earned_daily
            print(f"You now have {money} silver coins!")
            print()
            print(input("Press Enter to continue..."))
            os.system("cls")
        elif random_int == 3:
            earned_daily = random.randint(1,3)
            action_left -= 1
            print(f"You went to your usual spot for catching fish.")
            print(f"As expected, your local chef was exicted to have more product")
            print(f"For a few hours work, he paid you {earned_daily} silver coins")
            money += earned_daily
            print(f"You now have {money} silver coins!")
            print()
            print(input("Press Enter to continue..."))
            os.system("cls")

    elif chosen_job == professions[3]:
        if random_int == 1:
            earned_daily = random.randint(1,3)
            action_left -= 1
            print(f"You travel to your blackberry bushes to pick some blackberries.")
            print(f"The local chef was more than happy to take the berries off of your hands.")
            print(f"The tavern paid you {earned_daily} silver coins")
            money += earned_daily
            print(f"You now have {money} silver coins!")
            print()
            print(input("Press Enter to continue..."))
            os.system("cls")
        elif random_int == 2:
            earned_daily = random.randint(2,5)
            action_left -= 1
            print(f"Your neighbor told you about a funny looking plant he saw on his walk.")
            print(f"You decide to go gather the bush.")
            print(f"The local doctor tells you its a rare plant used to treat severe burns.")
            print(f"He pays you {earned_daily} for the funny looking plant!")
            money += earned_daily
            print(f"You now have {money} silver coins!")
            print()
            print(input("Press Enter to continue..."))
            os.system("cls")
        elif random_int == 3:
            earned_daily = random.randint(1,3)
            action_left -= 1
            print(f"You went to your usual spot for picking an assortment of plants.")
            print(f"As expected, your local chef was exicted to have more product")
            print(f"For a few hours work, he paid you {earned_daily} silver coins")
            money += earned_daily
            print(f"You now have {money} silver coins!")
            print()
            print(input("Press Enter to continue..."))
            os.system("cls")

def weapon_crafting():
        global iron_ingots
        global action_left
        global money
        global crafted_item

        item_name = ""
        item_quality = ""
        item_value = 0
        item_name = 0
        item_quality = 0

        item_name = random.randint(1,3)
        if item_name == 1:
            item_name = "Iron Dagger"
            item_value = item_value + 2
            req_ingots = 1
        elif item_name == 2:
            item_name = "Iron Sword"
            item_value = item_value + 4
            req_ingots = 2
        else:
            item_name = "Iron Mace"
            item_value = item_value + 6
            req_ingots = 3

        item_quality = random.randint(1,3)
        if item_quality == 1:
            item_quality = "Poor"
            item_value = item_value + 1
        elif item_quality == 2:
            item_quality = "Well-Made"
            item_value = item_value + 3
        else:
            item_quality = "Perfect"
            item_value = item_value + 5

        if iron_ingots == 0:
            print("You have no iron ingots! Try visiting the store to purchase some.")
            print(input("Press Enter to continue..."))
            os.system("cls")
        elif iron_ingots < req_ingots:
            action_left -= 1
            print(f"While attempting to craft a {item_name}, you relize you don't have enough iron ingots! Doings such a craft requires {req_ingots} iron ingots. You had {iron_ingots} and lost all of them!")
            iron_ingots = 0
            print(input("Press Enter to continue..."))
            os.system("cls")
        else:
            action_left -= 1
            print("You decide to craft an item of unknown quality")
            print(f"After many hours, you manage to craft a {item_quality} {item_name} worth {item_value}!")
            print(f"After selling it, you now have {money + item_value}")
            print(f"You used {req_ingots} iron ingot for this craft")
            iron_ingots -= req_ingots
            money = money + item_value
            print("")
            print(input("Press Enter to continue..."))
            os.system("cls")

def shop():
    global money
    global iron_ingots
    global meals

    while True:
        print("Welcome to the store! Spend your hard earned currency here!")
        print(f"You currently have {money} to spend:")
        print("")
        print("1. Buy iron ingot | $2 / each")
        print("2. Buy meal       | $2 / each")
        print("3. Back")
        print("")
        choice = input("What would you like to do?")
        os.system("cls")

        if choice == "1":
            choice = input(f"How many iron ingots would you like to purchase? (0 - {int(money/2)})")
            int_choice = int(choice)
            cost = int_choice * 2
            if choice == "0":
                print()
                os.system("cls")
            elif money >= cost:
                iron_ingots += int_choice
                money -= (int_choice * 2)
                print(f"You have purchased {choice} iron ingots. Your total iron ingots is now {iron_ingots}")
                print("")
                print(input("Press Enter to continue..."))
                os.system("cls")
            else:
                print("You don't seem to have enough currency for that!")
                print("")
                print(input("Press Enter to continue..."))
                os.system("cls")

        elif choice == "2":
            choice = input(f"How many meals would you like to purchase? (0 - {int(money/2)})")
            int_choice = int(choice)
            cost = int_choice * 2
            if choice == "0":
                print()
                os.system("cls")
            elif money >= cost:
                meals += int_choice
                money -= (int_choice * 2)
                print(f"You have purchased {choice} meals. Your total meals is now {meals}")
                print("")
                print(input("Press Enter to continue..."))
                os.system("cls")
            else:
                print("You don't seem to have enough currency for that!")
                print("")
                print(input("Press Enter to continue..."))
                os.system("cls")

        elif choice == "3":
            os.system("cls")
            break

def inventory():
    global iron_ingots
    global meals

    while True:
        print("1. Iron Ingots")
        print("2. Meals")
        print("3. Back")
        print("")
        choice = input("What would you like to check?")

        if choice == "1":
            os.system("cls")
            print(f"You currently have {iron_ingots} iron ingots!")
            print("")
            print(input("Press Enter to continue..."))
            os.system("cls")
        elif choice == "2":
            os.system("cls")
            print(f"You currently have {meals} meals!")
            print("")
            print(input("Press Enter to continue..."))
            os.system("cls")
        elif choice == "3":
            os.system("cls")
            break
        else:
            os.system("cls")

def dead():
    global char_name
    global days_survived

    print(f"GAME OVER")
    print(f"{char_name} survived {days_survived} day(s)!")
    print(input("Press Enter to continue..."))


def main():
    global meals
    global days_survived
    global isdead
    global action_left
    global hunger
    global char_name

    onStartup()

    while isdead == False:

        if action_left == 0:
            dead_chance = random.randint(1, 10)
            if dead_chance != 1:
                print("After a long day, you enter your house to go to bed.")
                time.sleep(2)
                if meals > 0:
                    meals -= 1
                    print(f"Before going to bed you decide to have a meal. Your hunger has been restored! You now have a total of {meals} meals")
                    time.sleep(2)
                    print("You made it through the night!")
                    print("")
                    print(input("Press Enter to continue..."))
                    os.system("cls")
                    action_left = 3
                    days_survived += 1
                    hunger = 0
                elif meals == 0 and hunger == 1:
                    print(f"Before going to bed you decided to have a meal, but you have none again! You enter a berzerk frenzy until one of the towns guards restrains you.")
                    print(f"Sadly, this is where your story ends. You will spend the last of your hungry existance behind bars.")
                    print(input("Press Enter to continue..."))
                    os.system("cls")
                    isdead = True
                    break
                elif meals == 0:
                    print(f"Before going to bed you decided to have a meal, but you have none! You decide to go to bed hungry...")
                    time.sleep(2)
                    print("You made it through the night!")
                    print("")
                    print(input("Press Enter to continue..."))
                    os.system("cls")
                    action_left = 3
                    days_survived += 1
                    hunger += 1

            else:
                print("You wake up to the sound of wood creaking...")
                time.sleep(1)
                print("By the time you realize you also hear footsteps, it's too late...")
                time.sleep(2)
                print("You exhale your last breath as the masked man drives a sword into your chest.")
                print("")
                isdead = True
                break


        print("1. Work")
        print("2. Craft Item")
        print("3. Shop")
        print("4. Check Inventory")
        print("")

        choice = input("What would you like to do?")

        os.system("cls")

        if choice == "1":
            daily_work()
        
        if choice == "2":
            weapon_crafting()
        
        if choice =="3":
            shop()
                        
        if choice =="4":
            inventory()

    dead()


main()
