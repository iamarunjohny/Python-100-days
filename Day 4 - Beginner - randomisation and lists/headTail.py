import random

getuserinput = input("Press 'T' to toss the coin🪙 and get results\n ").lower()
if getuserinput == 't':
    result = random.randint(1,2)
    if result==1:
        print("Heads")
    else:
        print("Tails")
else:
    print("You have to press 'T' or 't' to toss the coin")