class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        maxRes = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                res += 1
                maxRes = max(maxRes, res)
            else:
                res = 0
        return maxRes