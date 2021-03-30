import read_data_set as data_read


data = data_read.data
data = data.drop("Attribution", axis=1)
print("Modified Dataset : \n\n", data)


