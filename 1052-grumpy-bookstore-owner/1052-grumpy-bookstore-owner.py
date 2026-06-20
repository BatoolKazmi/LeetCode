class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0
        total = maxTotal = 0
        satisfied = 0

        for r in range(len(customers)):
            if grumpy[r]:
                total += customers[r]
            else:
                satisfied += customers[r]
            
            if r - l + 1 > minutes:
                if grumpy[l]:
                    total -= customers[l]
                l += 1
            
            maxTotal = max(total, maxTotal)
            
        return maxTotal + satisfied