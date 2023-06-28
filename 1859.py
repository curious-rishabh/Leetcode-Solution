x = s.split()
d = {}
for i in x:
    d[i[-1]] = i[:-1]
return ' '.join([d[j] for j in sorted(d)])