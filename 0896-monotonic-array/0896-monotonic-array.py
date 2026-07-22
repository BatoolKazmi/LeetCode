class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase = decrease = 0

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                increase += 1
            elif nums[i - 1] > nums[i]:
                decrease += 1
        
        if increase != 0 and decrease != 0:
            return False
        else:
            return True