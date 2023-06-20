# Brute Force - O(n2)
arr = []
for i in range(len(nums)):
    if nums.count(nums[i]) == 2 and nums[i] not in arr:
        arr.append(nums[i])
return arr

# Using dictionary and array - O(n)
nums = [4,3,2,7,8,2,3,1]
ans = []
hashmap = {}

for i in nums:
    hashmap[i] = hashmap.get(i,0) + 1
    
for key, value in hashmap.items():
    if value > 1:
        ans.append(key)
return ans