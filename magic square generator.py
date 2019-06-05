#generates magic squares of any odd size
import numpy as np

def set_matrix(n):
    matrix = np.random.randint(0,1,(n,n))*0
    matrix_list = np.arange(1,n+1,1,int)
    x = n-1
    y = int(np.median(matrix_list))-1
    matrix[x,y] = 1
    for value in range(2,n*n+1):
        if value % n != 1:
            x = (x + 1) % n
            y = (y + 1) % n
            matrix[x,y] = value
        elif value % n == 1:
            x = x - 1
            y = y
            matrix[x,y] = value
    return matrix

def matrix_sum(n):
    matrix_sum = int(((n**3) + n) / 2)
    return matrix_sum

def result(n):
    print(set_matrix(n))
    print(f"\nthe magic square sum is " + str(matrix_sum(n)))
    
result(9)
