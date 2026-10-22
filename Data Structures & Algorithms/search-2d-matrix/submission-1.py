class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.binarySearch(0, len(matrix)-1, matrix, target)

    def binarySearch(self, start, end, matrix, target):
        middle = (start + end) // 2
        
        if start > end:
            return False
        
        if matrix[middle][0] == target:
            return self.bs(0, len(matrix[middle])-1, matrix[middle], target)
        
        if matrix[middle][0] > target:
            return self.binarySearch(0, middle-1, matrix, target)

        elif matrix[middle][0] < target:
            return self.binarySearch(middle+1, end, matrix, target)

    def bs(self, start, end, array, target):
        middle = (start + end) // 2
        
        if start > end:
            return False
        
        if array[middle] == target:
            return True
        
        if array[middle] > target:
            return self.bs(0, middle-1, array, target)

        elif array[middle] < target:
            return self.bs(middle+1, end, array, target)