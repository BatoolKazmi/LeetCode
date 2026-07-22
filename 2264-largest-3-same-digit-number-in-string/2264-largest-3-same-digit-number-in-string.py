class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = -1
        count = 1

        for i in range(1, len(num)):
            if count != 3 and num[i -1] == num[i]:
                count += 1
            else:
                count =1
            if count == 3:
                count = 1
                res = max(res, int(num[i]))
        return f"{res}{res}{res}" if res != -1 else ""