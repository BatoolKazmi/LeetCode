class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = temp = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i -1]:
                temp += nums[i]
            else:
                temp = nums[i]
            res  = max(res, temp)
        return res