candies = [2,3,5,1,3]
extraCandies = 3

ans = []
maxx = max(candies)

for i in candies:
    if i + extraCandies >= maxx:
        ans.append(True)
    else:
        ans.append(False)
print(ans)