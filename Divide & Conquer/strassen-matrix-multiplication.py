import numpy as np

def divide(mat):
    x, y = mat.shape
    row2, col2 = x//2, y//2
    return mat[:row2, :col2], mat[:row2, col2:], mat[row2:, :col2], mat[row2:, col2:]


def squareMatrixMult(a,b):
    n=len(a)

    if (n==1):
        return a*b
    
    A11,A12,A21,A22=divide(a)
    B11,B12,B21,B22=divide(b)

    p1=squareMatrixMult(A11,B12-B22)
    p2=squareMatrixMult(A11+A12,B22)
    p3=squareMatrixMult(A21+A22,B11)
    p4=squareMatrixMult(A22,B21-B11)
    p5=squareMatrixMult(A11+A22,B11+B22)
    p6=squareMatrixMult(A12-A22,B21+B22)
    p7=squareMatrixMult(A11-A21,B11+B12)

    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2		
    c21 = p3 + p4		
    c22 = p1 + p5 - p3 - p7

    return np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))



if __name__ == '__main__':
    
    arr = np.array([[1, 2], [5, 6]])
    print(squareMatrixMult(arr,arr))
