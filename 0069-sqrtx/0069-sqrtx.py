class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x 
        res = 0

        while l <= r:
            mid = (l + r) // 2
            temp = mid * mid

            if temp > x:
                r = mid - 1
            else:
                l = mid + 1
                res = max(res, mid)
        return res