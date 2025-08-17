class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for index in range(9):
            x, y = index // 3, index % 3

            row = set()
            col = set()
            sqr = set()

            for idx in range(9):
                cell_row = board[index][idx]
                cell_col = board[idx][index]
                cell_sqr = board[x * 3 + idx // 3][y * 3 + idx % 3]

                if (cell_row in row or cell_col in col or cell_sqr in sqr):
                    return False
                
                if cell_row != '.': row.add(cell_row)
                if cell_col != '.': col.add(cell_col)
                if cell_sqr != '.': sqr.add(cell_sqr)
        
        return True