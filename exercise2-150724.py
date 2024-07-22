
import numpy as np


def compute_vector_length(vector):
    sum = 0
    for i in vector:
        sum += i**2
    return np.sqrt(sum)


def compute_dot_product(vector1, vector2):
    return np.dot(vector1, vector2)


def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result


def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result


def inverse_matrix(matrix):
    new_matrix = np.linalg.inv(matrix)
    return new_matrix


def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors


def compute_cosine(v1, v2):
    return np.dot(v1, v2)/(compute_vector_length(v1)*compute_vector_length(v2))


# cau 1
vector = np. array([-2, 4, 9, 21])
result = compute_vector_length(vector)
print('cau 1 ', result)

# cau 2
v1 = np. array([0, 1, -1, 2])
v2 = np. array([2, 5, 1, 0])
result = compute_dot_product(v1, v2)
print('cau 2 ', result)

# cau 3
x = np. array([[1, 2], [3, 4]])
k = np. array([1, 2])
print('cau 3 \n', x.dot(k))

# cau 4
x = np. array([[-1, 2], [3, -4]])
k = np. array([1, 2])
print('cau 4 \n', x@k)

# cau 5
m = np.array([[-1, 1, 1], [0, -4, 9]])
v = np.array([0, 2, 1])
result = matrix_multi_vector(m, v)
print('cau 5 ', result)

# cau 6
m1 = np. array([[0, 1, 2], [2, -3, 1]])
m2 = np. array([[1, -3], [6, 1], [0, -1]])
result = matrix_multi_matrix(m1, m2)
print('cau 6 ', result)

# cau 7
m1 = np.eye(3)
m2 = np. array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
result = m1@m2
print('cau 7 ', result)

# cau 8
m1 = np.eye(2)
m1 = np. reshape(m1, (-1, 4))[0]
m2 = np. array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1@m2
print('cau 8 ', result)

# cau 9
m1 = np. array([[1, 2], [3, 4]])
m1 = np. reshape(m1, (-1, 4), "F")[0]
m2 = np. array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1@m2
print('cau 9 ', result)

# cau 10
m1 = np. array([[-2, 6], [8, -4]])
result = inverse_matrix(m1)
print('cau 10 ', result)

# cau 11
matrix = np. array([[0.9, 0.2], [0.1, 0.8]])
eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(matrix)
print(eigenvectors)

# cau 12
x = np. array([1, 2, 3, 4])
y = np. array([1, 0, 3, 0])
result = compute_cosine(x, y)
print('cau 12 ', result)
