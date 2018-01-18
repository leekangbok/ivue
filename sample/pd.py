# import pandas as pd
#
#
# def pd_sample():
#     data = [("2015-04-20 11:17:21", 8100),
#             ("2015-04-17 11:36:21", 27000),
#             ("2015-04-17 11:36:13", 26000),
#             ("xxx", 3123),
#             ("adaf", 3465),
#             ("adfje", 62545),
#             ("adfae", 98285)]
#     df = pd.DataFrame(data, columns=['a', 'e'])
#     ma2 = df['e'].rolling(window=3).mean()
#     df.insert(len(df.columns), 'ma2', ma2)
#     print(df)
#
# import time
# t = '2017-12-12 12:59am'
# strt = time.strptime(t, '%Y-%m-%d %I:%M%p')
# print(type(strt))

# from sklearn.datasets import load_iris
from sklearn import tree

# iris = load_iris()
# print(iris.data)
# print(iris.target)

X = [[1, 2, 3], [4, 5, 2], [2, 1, 5], [2, 5, 3]]
Y = ['2b', '2b', '1s1b', '1s']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

r = clf.predict([[2, 4, 1]])
print(r)
