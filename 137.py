d = dict()
for i in nums:
    if i not in d:
        d[i] = d.get(i,0) + 1
    else:
        d[i] += 1

for key,value in d.items():
    if value == 1:
        return key