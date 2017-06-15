#encoding = utf-8
import numpy as np
from scipy import linalg as lg

arr = np.array([[1,2],[3,4]])
print "Det:",lg.det(arr)
print "Inv:",lg.inv(arr)
b = np.array([6,14])
print "Sol:",lg.solve(arr,b)
#矩阵的分解
print "LU:",lg.lu(arr)
print "OR:",lg.qr(arr)
print "SVD:",lg.svd(arr)
print "Schur:".lg.schur(arr)

if __name__ == "__main__":
    main()