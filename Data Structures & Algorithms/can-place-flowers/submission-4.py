class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for spot in range(len(flowerbed)):
            adjacent = []
            if flowerbed[spot] == 0 and n > 0:
                if spot+1 < len(flowerbed):
                    adjacent.append(spot+1)
                if spot-1 >= 0:
                    adjacent.append(spot-1)
                
                canPlant = True
                for neighbor in adjacent:
                    if flowerbed[neighbor] == 1:
                        canPlant = False
                
                if canPlant:
                    flowerbed[spot] = 1
                    n-=1
            
        return True if n <= 0 else False


        