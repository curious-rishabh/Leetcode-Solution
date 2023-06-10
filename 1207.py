arr = [1,2,2,1,1,3]

d = {}
for i in arr:
    d[i] = d.get(i,0) + 1 

lst = list(d.values())

l = {}

for key,value in d.items():
    if value in l:
        return False
    l[value] = 1
return True