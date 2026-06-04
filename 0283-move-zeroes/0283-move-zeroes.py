class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = t = 0

        while s < len(nums) and t < len(nums):
            if nums[t] != 0 and s != t:
                nums[s] = nums[t]
                nums[t] = 0
            if nums[s] != 0:
                s += 1
            t += 1
        