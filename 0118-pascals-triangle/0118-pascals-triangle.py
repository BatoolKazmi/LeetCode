class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        i = 0
        val = [1]

        while i != numRows:
           
            res.append(val)
            temp = []
            temp.append(1)
            for n in range(len(val)):
                if n + 1 > len(val) - 1:
                    temp.append(val[n])
                else:
                    temp.append(val[n] + val[n + 1])
            val = temp
            i += 1
        return res
                


        
