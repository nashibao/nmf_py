# -*- coding: utf-8 -*-
# 大規模疎行列 x 密行列演算の実行速度検証
# @nashibao

# 使い方:
# python mm_performance.py l1 l2 l3 alpha
# l1, l2: 疎行列サイズ
# l2, l3: 密行列サイズ
# alpha: 疎行列充填率
# sp_matrix(l1, l2, alpha) x dense_vec(l2, l3)

# 結果:
# 2013/01/22
# python mm_performance.py 100000 10000 10 0.005
# prepare..
#    0.437 sec
# compute..
#    0.067 sec
# python mm_performance.py 100000 100000 0.0005
# prepare..
#    0.428 sec
# 39.990176 Mbytes
# compute..
#    0.130 sec
# python mm_performance.py 3000000 10000 0.005
# prepare..
#   34.109 sec
# compute..
#    1.972 sec

# macbook pro retina 15inch
# 2.7 GHz Core i7
# 16GB 1600MHz DDR3
# OSX 10.8.2

from time import time
import numpy as np
import scipy.sparse as sp
from sys import argv, float_info


# 行列の準備
def prepare_matrices(l1=1000, l2=1000, alpha=0.1):
    # indexes and values of non-zero components
    # ii = np.random.randint(0, l, (int(l * l * alpha), 2))
    num = int(l1 * l2 * alpha)
    r = np.random.rand(num)
    i1 = np.random.randint(0, l1, size=num)
    i2 = np.random.randint(0, l2, size=num)

    # create a lil sparse matrix
    print "prepare.."
    t1 = time()
    # A = sp.coo_matrix((r, (i1, i2)), shape=(l, l))
    A = sp.csr_matrix((r, (i1, i2)), shape=(l1, l2))
    # A = sp.lil_matrix((l, l))
    # for n, i in enumerate(ii):
    #     A[i] = r[n]
    t2 = time()
    print "%8.3f sec" % (t2 - t1)
    print "%f Mbytes" % ((float)(A.data.nbytes) / 1000000)
    return A


def tests_sparse_matmul(A, vec):
    """
    compare speed of matrix product
    """
    print "compute.."
    t1 = time()
    A * vec
    t2 = time()
    print "%8.3f sec" % (t2 - t1)


if __name__ == "__main__":
    l1 = int(argv[1])
    l2 = int(argv[2])
    l3 = int(argv[3])
    alpha = float(argv[4])
    A = prepare_matrices(l1, l2, alpha)
    vec = np.random.rand(l2, l3)
    tests_sparse_matmul(A, vec)
