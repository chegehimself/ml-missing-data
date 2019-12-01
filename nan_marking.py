from pandas import read_csv
import numpy

dataset = read_csv('pima-indians-diabetes.data.csv', header=None)
# mark zero values as missing or NaN
dataset[[1, 2, 3, 4, 5]] = dataset[[1, 2, 3, 4, 5]].replace(0, numpy.NaN)
# print the first 20 rows of data
print(dataset.head(20))
