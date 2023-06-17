ans = []
i = 0
j = len(nums) // 2
for k in range(len(nums)//2):
    ans.append(nums[i])
    ans.append(nums[j])
    i += 1
    j += 1
return ans