import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

uchoice = input("What do you choose? type '0' for rock, '1' for paper, and '2' for scissor\n")
uchoice = int(uchoice)
if uchoice == 0:
    uchoice = rock
    print("\nYou choose rock")
elif uchoice == 1:
    uchoice = paper
    print("\nYou choose paper")
elif uchoice == 2:
    uchoice = scissors
    print("\nYou choose scissors")
else:
    print("select only '0', '1', or '2'")

print(uchoice)



robot=[rock,paper,scissors]
robotchoice=random.choice(robot)

print(robotchoice)

if uchoice == rock:
    if robotchoice == robot[0]:
        print ("robot choose rock\n\nrock = rock so it's a tie" )
    elif robotchoice == robot[1]:
        print ("robot choose paper\n\nrock < paper so you loose")
    elif robotchoice == robot[2]:
        print("robot choose scissors\n\nrock > scissors so you win")
elif uchoice == paper:
    if robotchoice == robot[0]:
        print ("robot choose rock\n\npaper > rock so you win" )
    elif robotchoice == robot[1]:
        print ("robot choose paper\n\npaper = paper so it's a tie")
    elif robotchoice == robot[2]:
        print("robot choose scissors\n\paper < scissors so you loose")
elif uchoice == scissors:
    if robotchoice == robot[0]:
        print ("robot choose rock\n\nscissors < rock so you loose" )
    elif robotchoice == robot[1]:
        print ("robot choose paper\n\nscissors > paper so you win")
    elif robotchoice == robot[2]:
        print("robot choose scissors\n\nscissors = scissors so it's a tie")