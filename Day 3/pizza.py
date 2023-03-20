print("Welcome to Python Pizza Deliveries🍕!")
bill = 0
size = input("What size pizza do you want? S, M, or L : ").lower()
if size=='s':
    bill +=15
elif size=='m':
    bill +=20
else:
    bill += 25

add_pepperoni = input("Do you want pepperoni? Y or N : ").lower()
if add_pepperoni=='y':
    if size=='s':
        bill += 2
    else:
        bill += 3

extra_cheese = input("Do you want extra cheese? Y or N : ").lower()
if extra_cheese=='y':
    bill+=1
print(f"Your final bill is 💰 {bill}")
