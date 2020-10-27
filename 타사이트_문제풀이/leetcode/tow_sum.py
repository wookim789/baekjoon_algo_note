class Solution(object):
    def twoSum(self, nums, target):
        
        for f in range(0, len(nums) - 1):
            for b in range(f + 1, len(nums)):
                if nums[f] + nums[b] == target:
                    return [f, b]


sol = Solution()

print(sol.twoSum([3,2,4], 6))
