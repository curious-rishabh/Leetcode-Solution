nums = [-2,1,-3,4,-1,2,1,-5,4]

max_val = nums[0]
temp = 0

for i in nums:
    if temp < 0:
        temp = 0            
    temp += i
    max_val = max(max_val, temp)

return max_val