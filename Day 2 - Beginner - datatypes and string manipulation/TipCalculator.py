print("Welcome to tip calculator")
bill = input("What was the bill? \n")
tip = input("What percentage tip would you like to give? 10, 12, or 15? \n")
noOFpeople = input ("How many people to split the bill? \n")
percent = ((float(tip)/100)*float(bill ))
total = percent + float(bill)
billWithTip = total/float(noOFpeople)
print(f"Each person should pay : {round(billWithTip)} ")