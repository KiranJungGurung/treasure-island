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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

first_step = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n')
first_lower_step = first_step.lower()
if first_lower_step == "left":
  #Continue the next step.
  second_step = input('You\'ve come to lake.There is an Island in the middle of the lake.Type " wait" to wait for the boat. Type "swim" to swim across.\n')
  second_lower_step = second_step.lower()
  if second_lower_step == "wait":
    #Continue the next step.
    third_step = input('You arrive at the Island unharmed. There is a house with three door. one red, one yellow, one blue. Which color do you choose?\n')
    third_lower_step = third_step.lower()
    if third_lower_step == "yellow":
      print("You found the treasure! You win!")
    elif third_lower_step == "red":
      print("It's room full of fire. Game Over.")
    elif third_lower_step == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("Game Over.")
  else:
    print("Yov've attacked by angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")