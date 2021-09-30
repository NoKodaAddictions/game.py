import os
from termcolor import colored
import random
from sys import exit

height = 10
width = 10
points = 0
coinrange = 5
rounds = 1
coins = []
enemyrange = 5
enemies = []

coordinates = [random.randint(0, width-1), random.randint(0, height-1)]

while True:
    flag = False
    for i in range(random.randint(1, enemyrange)):
        while True:
            while True:
                eheight = random.randint(0, height-1)
                if eheight == coordinates[1]:
                    continue
                else:
                    break

            while True:
                ewidth = random.randint(0, width-1)
                if ewidth == coordinates[0]:
                    continue
                else:
                    break

            for enemy in enemies:
                if eheight == enemy[1]:
                    if ewidth == enemy[0]:
                        flag = True
            if flag:
                continue
            else:
                print(ewidth, eheight)
                enemies.append([ewidth, eheight])
                break

    flag = False
    for i in range(random.randint(1, coinrange)):
        while True:
            while True:
                cheight = random.randint(0, height-1)
                if cheight == coordinates[1]:
                    continue
                else:
                    break

            while True:
                cwidth = random.randint(0, width-1)
                if cwidth == coordinates[0]:
                    continue
                else:
                    break

            for coin in coins:
                if cheight == coin[1]:
                    if cwidth == coin[0]:
                        flag = True
            if flag:
                continue
            else:
                print(cwidth, cheight)
                coins.append([cheight, cheight])
                break

    while True:
        os.system("cls")
        grid = []
        hit = False
        chit = False
        print(f"""
Width: {width}
Height: {height}
Enemies: {len(enemies)}
Coins Left: {len(coins)}
Coins Gathered: {points}
    """)
        for i in range(height):
            row = ""
            for j in range(width):
                flag = False
                eflag = False
                cflag = False
                if i == coordinates[1]:
                    if j == coordinates[0]:
                        flag = True
                for k in enemies:
                    if i == k[1]:
                        if j == k[0]:
                            eflag = True
                for l in coins:
                    if i == l[1]:
                        if j == l[0]:
                            cflag = True
                
                if eflag:
                    row += colored("[1]", 'red')
                elif cflag:
                    row += colored("[2]", "yellow")
                elif flag:
                    row += colored("[0]", 'green')
                else:
                    row += "[_]"
                

                    
            grid.append(row)
            
        for row in grid:
            print(row)
        
        inp = input("Go: ")
        if inp == "l":
            if coordinates[0]-1 < 0:
                pass
            else:
                coordinates[0] = coordinates[0] - 1
                
        elif inp == "r":
            if coordinates[0]+1 > width-1:
                pass
            else:
                coordinates[0] = coordinates[0] + 1
                
        elif inp == "u":
            if coordinates[1]-1 < 0:
                pass
            else:
                coordinates[1] = coordinates[1] - 1
                
        elif inp == "d":
            if coordinates[1]+1 > width-1:
                pass
            else:
                coordinates[1] = coordinates[1] + 1

        else:
            pass
        
        for enemy in enemies:
            if coordinates[0] == enemy[0]:
                if coordinates[1] == enemy[1]:
                    hit = True
        
        for coin in coins:
            print(coin)
            print(coordinates)
            if coordinates[0] == coin[0]:
                if coordinates[1] == coin[1]:
                    coins.remove(coin)
                    chit = True

        if hit:
            os.system("cls")
            print("You have hit an enemy, you died.")
            print(f"You got {points} points.")
            exit()
        elif chit:
            if points == points+len(coins):
                os.system("cls")
                print(f"You have won, congratulations!")
                
                print("Play again?")
                check = input("- ")
                if check == "y":
                    rounds += 1
                    print(f"Round {rounds}!")
                    input()
                    break
                else:
                    print("Thanks for playing!")
                    exit()
            else:
                points += 1
