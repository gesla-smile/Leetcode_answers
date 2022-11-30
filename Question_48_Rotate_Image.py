class Solution:
    def rotate(matrix):
        a = len(matrix)
        loop_number = a
        
        for m in range(loop_number): 
            for n in range(m, loop_number - m - 1):
                tmp = matrix[m][n]
                matrix[m][n]=matrix[loop_number-n-1][m]
                matrix[loop_number-n-1][m]=matrix[loop_number-m-1][loop_number-n-1]
                matrix[loop_number-m-1][loop_number-n-1]=matrix[n][loop_number-m-1]
                matrix[n][loop_number-m-1]=tmp              
        
        return matrix