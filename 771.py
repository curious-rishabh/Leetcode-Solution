# Brute Force
count = 0
for i in stones:
    for j in jewels:
        if i == j:
            count +=1
return count

# one line
return sum(i in J for i in S)