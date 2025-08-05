class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_triangle = [[1], [1, 1]]

        while len(pascal_triangle) < numRows:
            new_row = [1]
            
            for idx in range(1, len(pascal_triangle[-1])):
                num = pascal_triangle[-1][idx - 1] + pascal_triangle[-1][idx]
                new_row.append(num)
            else:
                new_row.append(1)
                pascal_triangle.append(new_row)
            
        return pascal_triangle[:numRows]