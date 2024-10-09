class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = {}

        for i, n in enumerate(nums):
            anw = target - n
            if anw in res:
                return[res[anw], i]
            res[n] = i
        