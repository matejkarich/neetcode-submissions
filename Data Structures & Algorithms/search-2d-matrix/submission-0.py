class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.binarySearch(0, len(matrix)-1, matrix, target)

    def binarySearch(self, start, end, matrix, target):
        middle = (start + end) // 2
        
        if start > end:
            return False
        
        for value in matrix[middle]:
            if value == target:
                return True
        
        if matrix[middle][0] > target:
            return self.binarySearch(0, middle-1, matrix, target)

        elif matrix[middle][0] < target:
            return self.binarySearch(middle+1, end, matrix, target)