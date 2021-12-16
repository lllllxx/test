import numpy as np

a = np.array([1, 2, 3])  # 使用列表构建一维数组
print(a)

print(type(a))
print("-" * 30)

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

print("-" * 30)
c = np.array([2, 4, 6, 8], dtype="complex")
print(c)
print("-" * 30)

arr = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [9, 10, 11, 23]])
print(arr.ndim)
print("-" * 30)
e = np.array([[1, 2], [3, 4], [5, 6]])
print("原数组", e)
e = e.reshape(2, 3)
print("新数组", e)
