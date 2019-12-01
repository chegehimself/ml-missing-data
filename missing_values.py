from pandas import read_csv

dataset = read_csv("pima-indians-diabetes.data.csv", header=None)
print(dataset.describe())
