from pandas import read_csv
import numpy
dataset = read_csv('pima-indians-diabetes.data.csv', header=None)
# print the first 20 rows of data
print(dataset.head(20))