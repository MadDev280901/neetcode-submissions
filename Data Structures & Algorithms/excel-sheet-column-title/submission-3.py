class Solution:
    def convertToTitle(self, colNumber: int) -> str:
        res = ""
        while colNumber > 0:
            res+=chr(ord('A') + (colNumber-1)%26)
            colNumber= (colNumber-1)//26
        
        return res[::-1]
        
    
        