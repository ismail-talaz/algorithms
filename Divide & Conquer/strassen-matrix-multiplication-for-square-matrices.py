import numpy as np             # MATRICES MUST BE SQUARE WITH EVEN-NUMBERED DIMENSONS.
                               # If N=2 --> θ(1)
                               # Else --> T(N)=7T(N/2)+θ(N^2)
def divide(mat):               # According to Master Theorem, we have T(N)=θ(N^(lg7)) which is faster than brute force θ(N^3) solution in pretty huge inputs.
    x, y = mat.shape           # However, another one is more advantageous when it comes to small inputs.
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
    p3=squareMatrixMult(A21+A22,B11)     # --> 7 recursive calls lead to T(N) = 7T(N/2)
    p4=squareMatrixMult(A22,B21-B11)
    p5=squareMatrixMult(A11+A22,B11+B22)
    p6=squareMatrixMult(A12-A22,B21+B22)
    p7=squareMatrixMult(A11-A21,B11+B12)

    c11 = p5 + p4 - p2 + p6            # --> Matrix addition and substraction is T(N) = θ(N^2)
    c12 = p1 + p2		
    c21 = p3 + p4		
    c22 = p1 + p5 - p3 - p7

    return np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))



if __name__ == '__main__':
    
    arr = np.array([[1, 2], [5, 6]])
    arr2= np.array([2,3],[8,7])
    print(squareMatrixMult(arr,arr2))
