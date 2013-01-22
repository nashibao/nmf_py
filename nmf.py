# -*- coding: utf-8 -*-
# gaussian-nmf

import numpy as np
import scipy.sparse as sp
from sys import float_info


class NMF(object):

    # ランダム疎行列
    def convert_sparse_matrix(self, data):
        s1, s2 = data.shape
        if s1 == 3:
            data = data.T
        vals = data[:, 2]
        rows = data[:, 0]
        cols = data[:, 1]
        n = rows.max()
        m = cols.max()
        A = sp.csr_matrix((vals, (rows, cols)), shape=(n + 1, m + 1))
        return A

    # ランダム疎行列
    def rand_sparse_matrix(self, n=10, m=10, alpha=0.1):
        num = int(n * m * alpha)
        vals = np.random.rand(num)
        rows = np.random.randint(0, n, size=num)
        cols = np.random.randint(0, m, size=num)
        A = sp.csr_matrix((vals, (rows, cols)), shape=(n, m))
        return A

    # セットアップ
    def setup(self, A, k=5):
        n, m = A.shape
        # sigma = ((float)(A.size)) / n / m
        W0 = np.random.rand(n, k)
        H0 = np.random.rand(k, m)

        self.errors = []
        self.A = A
        self.H = H0
        self.W = W0

        self.clusterH = None
        self.clusterW = None

    # nmf実行本体
    # iter_num: イタレーション回数
    # calc_error: エラー計算するかどうか．ここが一番重い
    # calc_error_num: 何回に1回エラー計算するか
    def run(self, iter_num=100, calc_error=False, calc_error_num=10):
        # 初期化
        H = self.H
        W = self.W
        eps = float_info.min
        A = self.A

        # イテレーション
        for i in range(1, iter_num):

            # update H
            # H=H.*(W'*A)./(W'*W*H+eps)
            H = H * ((A.T * W).T) / (W.T.dot(W).dot(H) + eps)
            # update W
            # W=W.*(A*H')./(W*(H*H')+eps);
            W = W * (A * H.T) / (W.dot(H.dot(H.T)) + eps)

            # エラー計算
            if i % calc_error_num != 0:
                continue
            print '.',
            if not calc_error:
                continue
            M = A - W.dot(H)
            error = np.multiply(M, M).sum()
            self.errors.append(error)
        self.H = H
        self.W = W

        print 'end'

    # W,Hから最大になった因数を取る
    def clusters(self):
        self.clusterH = np.argmax(self.H, 0)
        self.clusterW = np.argmax(self.W, 1)
