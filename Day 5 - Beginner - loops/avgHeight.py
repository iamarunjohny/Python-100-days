height= input("Enter heights : ").split()
height=[int(h) for h in height]
#To get total number of people who give height
numbr=0
for n in height:
    numbr+=1
#To get sum of all heights
total=0
for h in height:
    total=total+h
# print(f"total = {total}")
# total=sum(height)
avgh=total/(numbr)
print(f"Average height is {round(avgh)}")

