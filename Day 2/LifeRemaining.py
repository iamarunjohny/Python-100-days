age = input("Enter your age \n")
ageAsInt = int(age)

yearsRemaining = 90 - ageAsInt
monthsRemaining = yearsRemaining*12
weeksRemaining = monthsRemaining*4
daysRemaining = weeksRemaining*7

message = f"You have {yearsRemaining} years, {monthsRemaining} months, {weeksRemaining} weeks, {daysRemaining} days."
print(message)