# [Welcome Version Print]
print("On A Route v0.0.3")

# [Import]
import random

# [Set Player Stats]
playerHp = 100
playerDef = 10
playerAtk = 8
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
                    print("You take the left route")
                    break

                elif action == "idright":
                    print("You take the right route")
                    break

                else:
                    print("Invalid Command")

    elif action == "idcstat":
        print(f"Health: {playerHp}\n"
            f"Defense: {playerDef}\n"
            f"Attack: {playerAtk}\n"
            f"Distance: {playerDist}\n")
        
    else:
        print("Invalid Command\n")