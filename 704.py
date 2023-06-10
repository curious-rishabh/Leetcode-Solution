nums = [-1,0,3,5,9,12]
target = 13

low = 0
high = len(nums) -1

while low <= high:
    mid = (high + low) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] >= target:
        high = mid -1
    else:
        low = mid +1
return -1
