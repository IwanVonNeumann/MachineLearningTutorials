from sklearn import preprocessing, datasets

import dao

# data = dao.get_data()
diabetes = datasets.load_diabetes()
data = diabetes.data

print(len(diabetes.data))
print(len(diabetes.target))
print(diabetes.feature_names)

# for i in range(0, 10):
#     print(data[i])


# X = [x[:-1] for x in data]
# y = [x[-1] for x in data]
#
# # normalize the data attributes
# normalized_X = preprocessing.normalize(X)
#
# # standardize the data attributes
# standardized_X = preprocessing.scale(X)
#
# for i in range(0, 10):
#     print(X[i])
#     print(standardized_X[i])
#     print(normalized_X[i])
#     print()
