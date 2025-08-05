class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced_count = 0

        for fruit in fruits:
            for idx in range(len(baskets)):
                if fruit <= baskets[idx]:
                    del baskets[idx]
                    break
            else:
                unplaced_count += 1
        
        return unplaced_count