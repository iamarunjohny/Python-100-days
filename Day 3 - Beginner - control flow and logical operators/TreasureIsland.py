print(''' 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
direction = input(
    "Welcome to Tresure Island🏝️\nYour mission is to find the treasure🗺️.\nYou are at a cross road. Where do you want to go🧭? Type 'Left' or 'Right'\n").lower()

if direction == 'left':
    choose = input("\nYou've come to a lake. There is a island🏝️ in the middle of the lake. \nType 'Swim' to swim across🏊 or 'Wait' to wait for a boat⛵.\n")
    if choose == 'wait':
        door = input("\nYou arrived at the island unharmed. There is a house🏠 with 3 doors.One red, one yellow, and one blue.\n Which color do you choose? type 'Red', 'Blue', or 'Yellow'\n").lower()
        if door == 'red':
            print("It's a room full of fire. Game over🔥.")
        elif door == 'blue':
            print("You enter a room of beasts. Game Over.👾")
        elif door == 'yellow':
            print("You win!🏆")
        else:
            print("You chose a door that dosen't exist. Game over👾")
    else:
        print("You got attacked by an angry trout🐟. Game Over.")
else:
    print("You fell into a hole🕳️, Game over.")
