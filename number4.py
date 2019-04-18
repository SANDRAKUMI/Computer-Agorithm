import sys
import math
def matrix_mult(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][k] = (C[i][k] + A[i][j] * B[j][k]) % 100000
    return C
def fast_exponentiation(A, n):
    if n == 1:
        return A
    else:
        if n % 2 == 0:
            A1 = fast_exponentiation(A, n/2)
            return matrix_mult(A1, A1)
        else:
            return matrix_mult(A, fast_exponentiation(A, n - 1))

def solve(n):
    A = [[4, 13], [1, 4]]
    A_n = fast_exponentiation(A, n)
    return (2 * A_n[0][0] + 99999) % 100000


if __name__ == '__main__':
    t = input("Enter the number of cases: ")
    for i in range(int(t)):
        n = int(input()) 
        ret = solve(n)
        print('Case #%d: %05d' % (i+1, ret)) 
    
    


        



    
    


        

