s = ""
i = 0
while i < len(command):
    if command[i] =="G":
        s += "G"
        i +=1
    elif command[i:i+2] =="()":
        s += "o"
        i +=2
    else:
        s += "al"
        i +=4
return s