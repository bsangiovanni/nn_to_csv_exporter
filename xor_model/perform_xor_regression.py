from keras.models import Sequential
from keras.layers import Dense
import numpy as np

# Load the dataset for the XOR function
dataset = np.loadtxt('xor_model/xor_dataset.csv', delimiter=',')

x = dataset[:,0:2] # input
y = dataset[:,2] # labels

# NN with one layer with 2 neurons and a single output.
model = Sequential()
model.add(Dense(2, input_dim=2, activation='tanh'))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x, y, verbose=1, epochs=5000)

# Prediction results
results=model.predict(x)
print("Results:")
print(results)
print("Saving model to current directory...")
model.save("xor_model/xor_model.h5")
