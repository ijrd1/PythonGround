import numpy as np

"""
Scalar
- 数値
"""
s = 1

"""
Vector
- 数値が直線上に並ぶ
"""
v = np.array([-1.2, 0.41, 1.2e5])
print(v)

"""
Matrix
"""
m = np.array([[1, 2, 3],
              [4, 5, 6],
              [0.12, 8, -2.1]])

print(m)

"""
Tensor
- スカラーを複数の次元に並べたもの
- 各要素につく添字は, テンソルの階数となる
- スカラー(0階のテンソル), ベクトル(1階のテンソル), 行列(2階のテンソル)…
  行列を折り重なるように並べると3階のテンソル
"""

# (2, 3, 4) 3階のテンソル
t = np.array([[[0, 1, 2, 3],
               [2, 3, 4, 5],
               [4, 5, 6, 7]],

              [[1, 2, 3, 4],
               [3, 4, 5, 6],
               [5, 6, 7, 8]]])

print(t)
