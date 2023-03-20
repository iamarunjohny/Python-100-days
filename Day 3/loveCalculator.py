print("Welcome to love calculator❤️‍🔥")

name1 = input("\nWhat is your name?\n").lower()
name2 = input("What is their name?\n").lower()

# firstHalf = "True"
# secondHalf = "Love"

t = name1.count('t') + name2.count('t')
r = name1.count('r') + name2.count('r')
u = name1.count('u') + name2.count('u')
e = name1.count('e') + name2.count('e')

l = name1.count('l') + name2.count('l')
o = name1.count('o') + name2.count('o')
v = name1.count('v') + name2.count('v')
e = name1.count('e') + name2.count('e')

true = t+r+u+e
love = l+o+v+e

print(f"\ntotal no of 't''r''u''e' in both names = {true}\nt={t}\nr={r}\nu={u}\ne={e}")
print(f"total no of 'l''o''v''e' in both names = {love}\nl={l}\no={o}\nv={v}\ne={e}\n")

result=int(str(true)+str(love))
# result=int(result)

if result<10 or result>90:
    print(f"Your score is {result}, you go together like coke and mentos💥. ")
elif result>=40 and result<=50:
    print(f"Your score is {result}, you are alright together😍.")
else:
    print(f"Your score is {result} ❣️")
 
