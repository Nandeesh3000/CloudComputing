import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
height=[[3.0], [4.0],[5.0],[6.0],[7.0],[8.0],[9.0],[10.0]]
weight=[ 6, 8, 10, 12, 14, 16, 18, 20]
plt.scatter(height,weight,color='black')
plt.xlabel("height")
plt.ylabel("weight")
reg=linear_model.LinearRegression()
reg.fit(height,weight)
X_height=[[182.0]]
print(reg.predict(X_height))
