"""
print("Welcome to the tip calculator! ")
bill = float(input("What was the total bill? "))
tip = int(input("how much tip would you like to give? 10, 20, 30"))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay {final_amount}")
"""

# print("Welcome to the tip calculator! ")
# bill = float(input("what was the total bill? "))
# tip = int(input("How much tips would you like to give? 10 20 30"))
# people = int(input("How many people gonna share the bill? "))
# tip_as_percentage = tip / 100
# total_tip_amount = tip_as_percentage + bill
# bill_per_person = total_tip_amount / people
# final_amount = "{:.2f}".format(bill_per_person)
# print(final_amount)

# BAND NAME GENERATOR
# print("Welcome to the band name generator! ")
# city = input("What was the name of your city? ")
# pet = input("What was the name of your pet? ")
# band_name = city +  pet
# print(f"The band name we suggest is {band_name}")


# day 3 treasure island

print("Welcome to the world of treasure!")
print("To get the treasure u want to go in a right path.")
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

choice_1 = input('You are at a crossroad. where you wanna go? "left" or "right".').lower()

if choice_1 == 'left':
    choice_2 = input("you\'ve came near a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to  swim across the lake. ").lower()
    if choice_2 == 'wait':
        choice_3 = input("you\'ve arrive the island unharmed. There are 3 doors. The 'red', 'yellow' and 'blue'.which door would you choose?").lower()
        if choice_3 == 'red':
            print("You were attacked by Tribes. Game over.")
        if choice_3 == 'yellow':
            print("You were reached the treasure successfully!!")
        if choice_3 == 'blue':
            print("you were attacked by a hungry lion. Game over.")
        else:
            print("you chose a door that doesn't exist. Game over")
    else:
        print("You got attacked by an alligator")

else:
    print("you fell into a hole. Game over")

