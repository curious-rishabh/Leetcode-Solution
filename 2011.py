x = 0
for i in operations:
    if i == "++X":
        x +=1
    elif i == "X++":
        x +=1
    elif i == "--X":
        x -=1
    else:
        x -=1
return x