class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        List = []
        for i in range(0, len(self.nums)):
            if nums[i] + nums[i+1] == target:
                List.append([i,i+1])
        return List
    
nums = [2,7,11,15]
target = 9 

obj = Solution()
print(obj.twoSum(nums, target))