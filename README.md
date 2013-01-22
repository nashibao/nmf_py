# nmf_py

(Gaussian)NMF(Non-Negative Matrix Factorization) implementation on python.
This code is designed to handle large sparse matrix.

## usage.

```python
nmf = NMF()
A = nmf.rand_sparse_matrix(100000, 1000, 0.01)
nmf.setup(A, k=10)
nmf.run(iter_num=100)
nmf.clusters()
```
## performance

#### spec

 - macbook pro retina 15inch
 - mac 10.8.2
 - 2.7GHz corei7
 - 16GB memory
 - scipy superpack

#### setup
 - 1000000 x 10000 x 0.005 matrix
 - k=10
 - iter_num=100で

 ->
147.484 sec = 2.3 minutes