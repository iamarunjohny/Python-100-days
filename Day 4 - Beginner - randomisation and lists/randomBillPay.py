import random
names=input("Give me everybody's names seperated by a comma ', ' :\n").split(', ')
#split() will turn names into list
totalLength=len(names)
choosenOne=random.randint(0,totalLength-1)
result=names[choosenOne]
print(f"The chosen one is {result}")


#randon.choice(names) is easiest way to get this without all these codes above   //i mean names without .split(, )