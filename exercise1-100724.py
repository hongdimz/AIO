import pandas as pd
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# cau 1
arr_1 = np.arange(0, 10, 1)
print('cau 1')
print(arr_1)

# cau 2
arr_2_a = np.ones((3, 3)) > 0
arr_2_b = np.ones((3, 3), dtype=bool)
arr_2_c = np.full((3, 3), fill_value=True, dtype=bool)
print('cau 2')
print(arr_2_a)
print(arr_2_b)
print(arr_2_c)

# cau 3
print('cau 3')
arr_3 = np.arange(0, 10)
print(arr_3[arr_3 % 2 == 1])

# cau 4
print('cau 4')
arr_4 = np.arange(0, 10)
arr_4[arr_4 % 2 == 1] = -1
print(arr_4)

# cau 5
print('cau 5')
arr_5 = np.arange(0, 10)
arr_5_2d = arr_5.reshape(2, -1)
print(arr_5_2d)

# cau 6
arr_6_1 = np.arange(10).reshape(2, -1)
arr_6_2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr_6_1, arr_6_2], axis=0)
print('cau 6')
print(c)

# cau 7
arr_7_1 = np.arange(10).reshape(2, -1)
arr_7_2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr_7_1, arr_7_2], axis=1)
print('cau 7')
print(c)

# cau 8
arr_8 = np.array([1, 2, 3])
print('cau 8')
print(np.repeat(arr_8, 3))
print(np.tile(arr_8, 3))

# cau 9
arr_9 = np.array([2, 6, 1, 9, 10, 3, 27])
index_9 = np.where((arr_9 >= 5) & (arr_9 <= 10))
print('cau 9')
print(arr_9[index_9])

# cau 10


def maxx(x, y):
    if x > y:
        return x
    else:
        return y


a_10 = np.array([5, 7, 9, 8, 6, 4, 5])
b_10 = np.array([6, 3, 4, 8, 9, 7, 1])

pair_max = np.vectorize(maxx, otypes=[float])
print('cau 10')
print(pair_max(a_10, b_10))

# cau 11
a_11 = np.array([5, 7, 9, 8, 6, 4, 5])
b_11 = np.array([6, 3, 4, 8, 9, 7, 1])
print('cau 11')
print(np.where(a_11 < b_11, b_11, a_11))

# cau 12, 13, 14
print('cau 12, 13, 14')

img_12 = mpimg.imread(
    r'C:\Users\Admin\Documents\[Diem learning]\AIO Official\AIO\dog.jpeg')

img_12_lightness = (np.max(img_12, axis=2)+np.min(img_12, axis=2))/2
img_12_avg = np.mean(img_12, axis=2)

red, green, blue = img_12[:, :, 0], img_12[:, :, 1], img_12[:, :, 2]
img_12_lumi = np.array(red*0.21+green*0.72+blue*0.07)


# plt.imshow(img_12_lightness)
print(img_12_lightness[0, 0])
print(img_12_avg[0, 0])
print(img_12_lumi[0, 0])
# plt.imshow(img_12_avg)
# plt.imshow(img_12_lumi)

# plt.show()

# cau 15, 16, 17, 18, 19, 20
df = pd.read_csv(
    r'C:\Users\Admin\Documents\[Diem learning]\AIO Official\AIO\advertising.csv')

print('cau 15')
print(df['Sales'].max(), " - ", df['Sales'].idxmax())

print('cau 16')
print(df['TV'].mean())

print('cau 17')
print(df['Sales'][df['Sales'] >= 20].count())

print('cau 18')
print(df['Radio'][df['Sales'] >= 15].mean())

print('cau 19')
print(df['Sales'][df['Newspaper'] > df['Newspaper'].mean()].sum())

print('cau 20')
sales_avg = df['Sales'].mean()


print('cau 20')
scores = []
for _ in df['Sales']:
    if _ > sales_avg:
        scores.append('Good')
    elif _ == sales_avg:
        scores.append('Average')
    else:
        scores.append('Bad')
print(scores[7:10])
