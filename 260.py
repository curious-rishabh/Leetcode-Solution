d = dict()
for i in nums:
    if i not in d:
        d[i] = d.get(i,0) + 1
    else:
        d[i] += 1
count = []
for key,value in d.items():
    if value == 1:
        count.append(key)
return count