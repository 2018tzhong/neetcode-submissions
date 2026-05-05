class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, left, right, bottom = 0, 0, len(matrix[0])-1, len(matrix)-1

        results = []
        while top <= bottom and left <= right:
            # do one loop
            for i in range(left, right+1):
                results.append(matrix[top][i])
            
            for i in range(top+1, bottom+1):
                results.append(matrix[i][right])

            if top == bottom:
                break

            for i in range(right-1, left-1, -1):
                results.append(matrix[bottom][i])
            
            if left == right:
                break

            for i in range(bottom-1, top, -1):
                results.append(matrix[i][left])

            top += 1
            left += 1
            bottom -= 1
            right -= 1

        return results