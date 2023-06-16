arr = []
summ = 0
for i in range(len(nums)):
    if i == 0:
        arr.append(nums[0])
        summ += nums[i]
        continue
    summ += nums[i]
    arr.append(summ)
return arr