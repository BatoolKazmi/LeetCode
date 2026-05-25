class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, fast = 0, 0
        k = 1 if len(nums) > 0 else 0

        while (i < len(nums) and fast < len(nums)):
            if nums[i] < nums[fast]:
                nums[i + 1] = nums[fast]
                k += 1
                i += 1
            elif nums[i] == nums[fast]:
                fast += 1
        return k
        