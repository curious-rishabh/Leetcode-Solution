maxx = 0
for i in sentences:
    maxx = max(len(i.split()), maxx)
return maxx