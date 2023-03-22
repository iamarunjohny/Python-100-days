row1 = ["🎁","🎁","🎁"] 
row2 = ["🎁","🎁","🎁"] 
row3 = ["🎁","🎁","🎁"] 

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
# print(map)
position = input("Where do you want to put the treasure?💰")

position = int(position)

if position>33:
     print("Maximum 33")
else:
     position=str(position)
     horizontal=(int(position[0]))
     vertical=(int(position[1]))
     selectedRow=map[vertical-1]
     selectedRow[horizontal-1]='❎'
     #or we can use "map[vertical -1][horizontal -1]= '❎'"  insted of 'selectedRow=map[vertical-1]''selectedRow[horizontal-1]='❎''
     print(f"{row1}\n{row2}\n{row3}")

# print(map[horizontal-1])

# if horizontal or vertical>3:

