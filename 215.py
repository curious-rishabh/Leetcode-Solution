# nums = [3,2,1,5,6,4] 
# k = 2

nums = [3,2,3,1,2,4,5,5,6]
k = 1

nums.sort()

largest = max(nums)

j = 0

for i in range(len(nums)-1,-1,-1):
    if largest >= nums[i]:
        largest = nums[i]
        # print(nums[i])
        j+= 1
    if j == k:
        print(largest)
        