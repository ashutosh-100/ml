from sklearn.linear_model import LinearRegression
import numpy as np
X = np.array([[20], [25], [30], [35]])   # temperatures
y = np.array([100, 150, 200, 250])       # ice cream sales
model = LinearRegression()   # create the brain
model.fit(X, y)              # train the brain
print(model.predict([[40]]))  # ask: what about 40°C?