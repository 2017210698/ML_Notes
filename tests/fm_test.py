import numpy as np
import os

os.chdir('../')
import matplotlib.pyplot as plt
from ml_models.fm import FM

# data1 = np.linspace(1, 10, num=10000)
# data2 = np.linspace(1, 10, num=10000) + np.random.random(size=10000)
# data3 = np.linspace(10, 1, num=10000)
# target = data1 * 2 + data3 * 0.1 + data2 * 1 + 10 * data1 * data2 + np.random.random(size=10000)
# data = np.c_[data1, data2, data3]

data = np.random.random((50000, 25))
data = np.c_[np.linspace(0, 1, 50000), data]
target = data[:, 0] * 1 + data[:, 1] * 2 + 2 * data[:, 8] * data[:, 9]

from ml_models.wrapper_models import DataBinWrapper

binwrapper = DataBinWrapper()
binwrapper.fit(data)
new_data = binwrapper.transform(data)

from sklearn.preprocessing import OneHotEncoder

one_hot_encoder = OneHotEncoder()
new_data = one_hot_encoder.fit_transform(new_data).toarray()
print(new_data.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(new_data, target, test_size=0.4, random_state=0)

model = FM(batch_size=128)
train_losses,eval_losses=model.fit(X_train, y_train, eval_set=(X_test, y_test))

plt.scatter(data[:, 0], target)
plt.plot(data[:, 0], model.predict(new_data), color='r')
plt.show()
plt.plot(range(0,len(train_losses)),train_losses,label='train loss')
plt.plot(range(0,len(eval_losses)),eval_losses,label='eval loss')
plt.legend()
plt.show()
print(model.V)
print(model.w)
