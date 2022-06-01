import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from sklearn import datasets
from sklearn.mixture import GaussianMixture


iris = datasets.load_iris()
X = iris.data[:, :2]
d = pd.DataFrame(X)
plt.grid()
plt.scatter(d[0], d[1])
plt.title("Before Clustering")
plt.xlabel('sepallength')
plt.ylabel('sepalwidth')




gmm = GaussianMixture(n_components = 3)
gmm.fit(d)
labels = gmm.predict(d)
d['labels']= labels
d0 = d[d['labels']== 0]
d1 = d[d['labels']== 1]
d2 = d[d['labels']== 2]
plt.grid()
plt.scatter(d0[0], d0[1], c ='r')
plt.scatter(d1[0], d1[1], c ='yellow')
plt.scatter(d2[0], d2[1], c ='g')
plt.title("After Clustering using E-M clustering")
plt.xlabel('sepallength')
plt.ylabel('sepalwidth')
