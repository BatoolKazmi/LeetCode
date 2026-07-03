class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = dec = 1
        res = 1

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                inc += 1
                dec = 1
            elif nums[i] > nums[i + 1]:
                dec += 1
                inc = 1
            else:
                dec = inc = 1
            
            res = max(res, inc, dec)

        return res