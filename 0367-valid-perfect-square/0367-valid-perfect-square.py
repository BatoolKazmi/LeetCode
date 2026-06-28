class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num

        while l <= r:
            mid = (l + r) // 2
            temp = mid * mid

            if temp > num:
                r = mid - 1
            elif temp < num:
                l = mid + 1
            else:
                return True
        return False