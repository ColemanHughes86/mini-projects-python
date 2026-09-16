import random

warrior_health = 100
warrior_damage = 20
warrior_speed = 10
warrior_range = 1

mage_health = 50
mage_damage = random.randint(10, 30)
mage_speed = 5
mage_range = 10

rogue_health = 30
rogue_damage = 15
rogue_speed = 20
rogue_range = 2

goblin_arm_health = 15
goblin_speed = 8

fox_health = 18

coins = 0

character = input("Welcome to my story game! Type your character's name: ")

print(f"Welcome, {character}! We are going to set up your playstyle.")

class_choice = input("Choose your class: Warrior, Mage, or Rogue.\nWarriors are tanky with high damage but low speed and range.\nMages have high range and variable damage but low health and speed.\nRogues have short range and low health but high speed and damage.\nChoose: ")

if class_choice.lower() == "warrior":
    health = warrior_health
    damage = warrior_damage
    speed = warrior_speed
    range_ = warrior_range
    print(f"You have chosen the Warrior class! Your stats are:\nHealth: {health}\nDamage: {damage}\nSpeed: {speed}\nRange: {range_}")
elif class_choice.lower() == "mage":
    health = mage_health
    damage = mage_damage
    speed = mage_speed
    range_ = mage_range
    print(f"You have chosen the Mage class! Your stats are:\nHealth: {health}\nDamage: {damage}\nSpeed: {speed}\nRange: {range_}")
elif class_choice.lower() == "rogue":
    health = rogue_health
    damage = rogue_damage
    speed = rogue_speed
    range_ = rogue_range
    print(f"You have chosen the Rogue class! Your stats are:\nHealth: {health}\nDamage: {damage}\nSpeed: {speed}\nRange: {range_}")
else:
    print("Invalid class choice. Please restart the game and choose a valid class.")
    exit()


print("Now that you have chosen your class, let's begin your adventure!\nYou live in an average village with creatures of all kinds.\nOne day, when going to meet your defense trainer, you hear a sudden explosion.")
explosion_choice = input('Do you want to go torwards the explosion or away from it? (Type "towards" or "away"): ')

if explosion_choice.lower() == "towards":
    print('You run through the village hearing screams from all around.\nAnd as you get closer to the explosion, smoke starts blocking your vision.\nSuddenly you get knocked to the ground from behind.')
    leg_choice =input('You feel something grab your leg, you can either attack or try to run away. (Type "attack" or "run"): ')
    if leg_choice.lower() == 'attack':
        if class_choice.lower == 'mage':
            damage = random.randint(10, 30)
        goblin_arm_health -= damage
        if goblin_arm_health <= 0:
            print('You slice the goblins arm off scaring away the goblin tribe as they scream in agony.\nYou have survived the encounter and continue your adventure.')
            print('Your village is proud of your bravory and hold the cerimony of truth for you.\nYour master has finally seen your potential and decides to give you a mission')
            mission_acceptance = input('Oh how much you have grown little challenger.\nI wish for you to go on a mission and save the captured princess in the tower of HELL.\n Yes or N0 (Y/N): ')
            if mission_acceptance.lower() == 'y':
                print('Very well kid, I will make the preparations for your journey.')
                print('You are given five coins and set of down the old stone path')
                coins += 5
                direction = input('You see a sign that says Tower of Hell point left when two paths intersect. Enter Left/Right')
                if direction.lower() == 'left':
                    print('You head down and odd looking path and feel as if someone is watching you.')
                    print('Suddenly you step on trap that makes you fall into a pit of spikes. -25 health')
                    health -= 25
                    help_choice = input('As your climbing out you see a fox walk by and he asks if you need help. Yes or No (Y/N)')
                    if help_choice.lower == ('y'):
                        print('The fox steals your money and pushes you back into the hole.\n you quickly try to escape but a boulder rolls down the path crushing you.\n You were caught by the sly fox')
                        health -= health
                    elif help_choice.lower() == ('n'):
                        fox_survival_choice = input('You can tell somethings fishy and with a short time to react you must choose something.\nType one option (attack, nothing, pull)')
                        if fox_survival_choice.lower() == 'attack':
                            if class_choice.lower == 'mage':
                                damage = random.randint(10, 30)
                            if fox_health - damage <= 0:
                                print('You defeated the fox and made it out of the whole continuing on your journey.')
                            elif fox_health - damage >0: 
                                health -= 25
                                coins -= 5
                                print("You couldn't deal enough damage, the fox steals your money attacks you and runs. - 25 health. - 5 coins.")
                                print('You make it out of the whole with not much to spare')
                        elif fox_survival_choice.lower() == 'nothing':
                            coins -= 5
                            health -= health
                            print('The fox catches you off gaurd when you did not react.\nHe takes your money and pushes you back into the whole before a boulder crushes you.')
                        elif fox_survival_choice.lower() == 'pull':
                            print('You pull the fox in and as you brawl it out a boulder set as a trap crushes you.')
                            health -= health
            elif mission_acceptance.lower() == 'n':
                print('You may live the rest of your life in this village peacefully. Happy Ending')
                exit()
        else:
            print('The damage was not enough to defeat the goblin.\nThey hold you captive and make you watch as they destroy your village.\nYou are taken to their layer with little plans of escape. -10 health')
            health -= 10
    elif leg_choice.lower() == 'run':
        if speed > goblin_speed:
            print('You manage to break free from the goblins grip and run away.\nYou make it out torwards the forest safely but are shaken with the fact that you were unable to save your village.\n -2 health')
            health -= 2
        if speed <= goblin_speed:
            print('You try to run away but the goblin is faster than you.\nThey hold you captive and make you watch as they destroy your village.\nYou are taken to their layer with little plans of escape. -10 health')
            health -= 10
elif explosion_choice.lower() == "away":
    print('You head away from the explosion, and have the choice of going torwards the woods or back home.')
    location_choice = input('Do you want to go torwards the woods or back home? (Type "woods" or "home"): ')
    if location_choice.lower() == 'woods':
        print('You head torwards the woods safely but watch as your village is destroyed from a distance.\nYou are shaken with the fact that you were unable to save your village.\n -2 health')
        health -= 2
    elif location_choice.lower() == 'home':
        print('You head home but the goblins have already caught it on fire.\nYou watch as your family is killed and the goblins come for you.!!!')
        health -= health

if health <= 0:
    print("You have no health left. Game over.")
    exit()