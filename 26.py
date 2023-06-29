# Brute Force Method
nums = [1,1,2]
# O/P: 2, nums = [1,2,_]
expectedNums = sorted(list(set(nums)))
k = len(expectedNums)
for i in range(len(expectedNums)):
    nums[i] = expectedNums[i]
    
return len(expectedNums)

# using pop()
i = 1
while i < len(nums):
    if nums[i] == nums[i - 1]:
        nums.pop(i)
    else:
        i += 1
return len(nums)