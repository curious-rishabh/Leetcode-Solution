for i in range(0,len(nums)-1):
    if nums[i] == nums[i+1]:
        nums[i] = nums[i]*2
        nums[i+1] = 0
# Move zero to last
i = 0
for j in range(len(nums)):
    if nums[i] == 0 and nums[j] !=0:
        nums[i], nums[j] = nums[j], nums[i]

    if nums[i] != 0:
        i +=1
return nums