from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

import dao

data = dao.get_data()

n = len(data)

X = [x[:-1] for x in data]
y = [x[-1] for x in data]

model = LogisticRegression()

# create the RFE model and select 3 attributes
rfe = RFE(model, 3)
rfe = rfe.fit(X, y)

# summarize the selection of the attributes
print(rfe.support_)
print(rfe.ranking_)
