import random
import time
import os

print("Welcome to The Blacksmith")
print("You will live the simple life of a blacksmith")
print("Work, craft items, and sell them")
print("")
print(input("Press Enter to continue..."))
os.system("cls")

dead = False
money = 0
action_left = 3
days_survived = 0
iron_ingots = 0
meals = 0
req_ingots = 0
hunger = 0


while dead == False:

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
                dead = True
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
            dead = True
            break


    print("1. Work")
    print("2. Craft Item")
    print("3. Shop")
    print("4. Check Inventory")
    print("")

    choice = input("What would you like to do?")

    os.system("cls")

    if choice == "1":
        action_left -= 1
        days_work = random.randint(1, 8)
        print(f"You go to work and earn {days_work}. Your total is now {days_work + money}" )
        money = days_work + money
        print("")
        print(input("Press Enter to continue..."))
        os.system("cls")
    
    if choice == "2":
        item_name = ""
        item_quality = ""
        item_value = 0
        item_name = 0
        item_quality = 0
        crafted_item = [item_name, item_quality, item_value]
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
    
    if choice =="3":
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
                    
    if choice =="4":
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


print(f"GAME OVER")
print(f"You survived {days_survived} days!")
print(input("Press Enter to continue..."))



#IDEAS

#For every day you dont rest, increase chance of death += 1
#Remove Work function