nums = [0,1,4,5,0,3,12]

# Takings Extra Space
arr2 = []
count = 0
for i in range(len(nums)):
    if nums[i] == 0:
        count +=1
        pass
    else:
        arr2.append(nums[i])
for i in range(count):
    arr2.append(0)
    
# Without extra space using 2 pointer
i = 0
for j in range(len(nums)):
    if nums[i] == 0 and nums[j] != 0:
        nums[i] , nums[j] = nums[j] , nums[i]
    
    if nums[i] != 0:
        i +=1