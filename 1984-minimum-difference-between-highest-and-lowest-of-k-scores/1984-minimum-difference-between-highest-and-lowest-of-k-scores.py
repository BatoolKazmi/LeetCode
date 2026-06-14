class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        nums.sort()
        res = float("inf")

        while r < len(nums):
            if r - l == k - 1:
                diff = nums[r] - nums[l]
                res = min(res, diff)
                l += 1
            r += 1
        return res
        