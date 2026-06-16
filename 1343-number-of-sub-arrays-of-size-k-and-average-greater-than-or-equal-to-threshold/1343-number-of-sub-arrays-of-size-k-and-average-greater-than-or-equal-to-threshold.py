class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, 0
        res = 0
        total = 0

        while r < len(arr):
            total += arr[r]

            if r - l == k - 1:
                avg = total / k
                res += 1 if avg >= threshold else 0
                total -= arr[l]
                l += 1
            r += 1
        return res