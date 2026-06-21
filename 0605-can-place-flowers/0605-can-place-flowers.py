class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        for i in range(len(flowerbed)):
            left_ok = (i == 0) or (flowerbed[i-1] == 0)
            right_ok = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)
            if flowerbed[i] == 0 and left_ok and right_ok:
                count += 1 
                flowerbed[i] = 1

        return count >= n