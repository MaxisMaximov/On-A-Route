# [Welcome Version Print]
print("On A Route v0.0.2")

# [Set Player Stats]
playerHp = 100
playerDef = 10
playerAtk = 8

# [Main Loop]
while True:
    action = input("Move: idmov\n"
    "Check Stats: idcstat\n")

    if action == "idmov":
        print("You moved\n")

    elif action == "idcstat":
        print(f"Health: {playerHp}\n"
            f"Defense: {playerDef}\n"
            f"Attack: {playerAtk}\n")
        
    else:
        print("Invalid Command\n")