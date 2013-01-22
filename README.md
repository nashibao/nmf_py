# nmf_py

(Gaussian)NMF(Non-Negative Matrix Factorization) implementation on python.
This code is designed to handle large sparse matrix.

## usage.

```python
nmf = NMF()
// random sparse matrix
A = nmf.rand_sparse_matrix(100000, 1000, 0.01)
nmf.setup(A, k=10)
nmf.run(iter_num=100)
// hard clustering
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

 - sparse matrix size: 1000000 x 10000
 - density: 0.005
 - hidden variable num: 10
 - iter_num: 100

 ->
`147.484` sec = `2.3` min