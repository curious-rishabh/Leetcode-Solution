# Brute Force -> O(n2)

ans = []
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] > nums[j]:
            count +=1
    ans.append(count)
return ans