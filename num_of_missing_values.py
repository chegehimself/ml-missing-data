from pandas import read_csv

dataset = read_csv('pima-indians-diabetes.data.csv', header=None)

print((dataset[[1, 2, 3, 4, 5]] == 0).sum())
