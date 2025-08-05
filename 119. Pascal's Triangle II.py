class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
    
        for number_row in range(rowIndex):
            prev_row, row = row, [1] + [0] * number_row + [1]

            for idx in range(1, len(prev_row)):
                row[idx] = prev_row[idx - 1] + prev_row[idx]
            
        return row