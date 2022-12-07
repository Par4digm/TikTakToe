import random
import time
import pdb

global row_1
global row_2
global row_3
row_1 = list(['_','_','_'])
row_2 = list(['_','_','_'])                 #The game board
row_3 = list(['_','_','_'])

######## GAME EVENTS ######## 

def ChooseSide():
    global player_symbol
    global enemy_symbol
    player_symbol = (str(input('Enter your team (X/O): '))).upper()

    if player_symbol == 'X':
        enemy_symbol = 'O'
    else:
        enemy_symbol = 'X'

def ShowBoard(r1, r2, r3):
    print(r1)
    print(r2)
    print(r3)

def CheckForWin(r1, r2, r3, player_symbol, enemy_symbol):

    if (r1[0] == r2[1]) and (r1[0] == r3[2]) and (r1[0] == player_symbol):       
        return True
    elif (r1[2] == r2[1]) and (r1[2] == r3[0]) and (r1[2] == player_symbol):
        return True    
    elif (r1[0] == r1[1]) and (r1[0] == r1[2]) and (r1[2] == player_symbol):    
        return True
    elif (r2[0] == r2[1]) and (r2[0] == r2[2]) and (r2[2] == player_symbol):
        return True
    elif (r3[0] == r3[1]) and (r3[0] == r3[2]) and (r3[2] == player_symbol):
        return True
    elif (r1[0] == r2[0]) and (r1[0] == r3[0]) and (r1[0] == player_symbol):
        return True
    elif (r1[2] == r2[2]) and (r1[2] == r3[2]) and (r1[2] == player_symbol):
        return True
    elif (r1[0] == r2[1]) and (r1[0] == r3[2]) and (r1[0] == enemy_symbol):       
        return False
    elif (r1[2] == r2[0]) and (r1[2] == r3[0]) and (r1[2] == enemy_symbol):
        return False    
    elif (r1[0] == r1[1]) and (r1[0] == r1[2]) and (r1[2] == enemy_symbol):    
        return False
    elif (r2[0] == r2[1]) and (r2[0] == r2[2]) and (r2[2] == enemy_symbol):
        return False
    elif (r3[0] == r3[1]) and (r3[0] == r3[2]) and (r3[2] == enemy_symbol):
        return False
    elif (r1[0] == r2[0]) and (r1[0] == r3[0]) and (r1[0] == enemy_symbol):
        return True
    elif (r1[2] == r2[2]) and (r1[2] == r3[2]) and (r1[2] == enemy_symbol):
        return True
    else:
        return "NotYet"


def PlayerPlay(r1, r2, r3, player_symbol):

    PossiblePlay = False

    while PossiblePlay == False:

        row_play = input('Choose your row: ')
        columns_play = int(input('Choose your colomn: ')) - 1

        if row_play == str(1):
            if (r1[columns_play] == "_"):
                row_1[columns_play] = player_symbol
                #pdb.set_trace()
                PossiblePlay = True 
            else:
                PossiblePlay = False
                print("") 
                print("Play was already made in this position :/")
                print("") 

        elif row_play == str(2):
            if (r2[columns_play] == "_"):
                row_2[columns_play] = player_symbol
                PossiblePlay = True 
            else:
                PossiblePlay = False
                print("") 
                print("Play was already made in this position :/")
                print("") 

        elif row_play == str(3):
            if (r3[columns_play] == "_"):
                row_3[columns_play] = player_symbol
                PossiblePlay = True 
            else:
                PossiblePlay = False
                print("") 
                print("Play was already made in this position :/")
                print("") 

def EnemyPlay(r1, r2, r3, enemy_symbol):

    PossiblePlay = False     

    while not PossiblePlay:
        row_play = random.randint(1, 3)
        column_play = random.randint(0, 2)

        if row_play == 1:
            if (r1[column_play] == "_"):
                row_1[column_play] = enemy_symbol
                PossiblePlay = True 
            else:
                PossiblePlay = False 

        elif row_play == 2:
            if (r2[column_play] == "_"):
                row_2[column_play] = enemy_symbol
                PossiblePlay = True 
            else:
                PossiblePlay = False

        elif row_play == 3:
            if (r3[column_play] == "_"):
                row_3[column_play] = enemy_symbol
                PossiblePlay = True 
            else:
                PossiblePlay = False

######## CURRENT GAME ######## 

runGame = True                   

ChooseSide()

while runGame:
    #Game loop
    ShowBoard(row_1, row_2, row_3)

    PlayerPlay(row_1, row_2, row_3, player_symbol)

    if CheckForWin(row_1, row_2, row_3, player_symbol, enemy_symbol) == True:
        print("")
        print("YOU WON THE GAME!!!")
        print("")
        runGame = False
        break
    elif CheckForWin(row_1, row_2, row_3, player_symbol, enemy_symbol) == False:
        print("")
        print("you lost ;-;")
        print("")
        runGame = False
        break
    elif CheckForWin(row_1, row_2, row_3, player_symbol, enemy_symbol) == "NotYet":
        runGame = True

    ShowBoard(row_1, row_2, row_3)
    
    print("")
    print("Enemy's Turn")
    print("")

    EnemyPlay(row_1, row_2, row_3, enemy_symbol)

    if CheckForWin(row_1, row_2, row_3, player_symbol, enemy_symbol) == True:
        print("")
        print("YOU WON THE GAME!!!")
        print("")
        runGame = False
        #break
    elif CheckForWin(row_1, row_2, row_3, player_symbol, enemy_symbol) == False:
        print("")
        print("you lost ;-;")
        print("")
        runGame = False
        #break
    elif CheckForWin(row_1, row_2, row_3, player_symbol, enemy_symbol) == "NotYet":
        runGame = True

    time.sleep(5)

input("Type any key to exit...")

