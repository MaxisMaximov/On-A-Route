# [Welcome Version Print]
print("On A Route v0.0.4")

# [Import]
import random

# [Set Player Stats]
playerHp = 50
playerDef = 10
playerAtk = 4
playerDist = 0

# [Main Loop]
while True:
    action = input("Move: idmov\n"
    "Check Stats: idcstat\n")

    if action == "idmov":
        print("You moved\n")
        playerDist += 10

        fork = random.randint(0,4) # Roll a chance for a road fork
        if fork < 1:
            while True:
                action = input("You encounter a road fork\n"
                "Left route: idleft\n"
                "Right route: idright\n")

                if action == "idleft":
                    print("You take the left route\n")
                    break

                elif action == "idright":
                    print("You take the right route\n")
                    break

                else:
                    print("Invalid Command\n")

        monster = random.randint(0,4) # Roll a chance for a monster
        if monster < 1:
            # Set Monster HP and Attack values
            monsterHp = random.randint(4, 10)
            monsterAtk = random.randint(2, 6)

            print(f"A monster with {monsterHp} HP and {monsterAtk} Attack appears!\n"
            "Warning: Invalid commands won't result in action\n") # Some punishment must be made lol
            while True:
                action = input("Attack: idatk")

                if action == "idatk":
                    monsterHp -= playerAtk
                    print("You attack the monster!\n"
                    f"Damage dealt: {playerAtk}\n"
                    f"Health remaining (Monster): {monsterHp}\n")
                    if monsterHp < 1:
                        print("You win!\n")
                        break
                else:
                    print("Invalid Command\n")

                playerHp -= monsterAtk
                print("The monster attacks!\n"
                f"Damage dealt: {monsterAtk}\n"
                f"Health remaining (You): {playerHp}\n")
                if playerHp < 1:
                    print("Game Over")
                    exit


    elif action == "idcstat":
        print(f"Health: {playerHp}\n"
            f"Defense: {playerDef}\n"
            f"Attack: {playerAtk}\n"
            f"Distance: {playerDist}\n")
        
    else:
        print("Invalid Command\n")