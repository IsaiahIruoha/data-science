import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataset = pd.read_csv('unclean-wine-quality.csv')
dataset = dataset.iloc[:, 1:-1]
nan_indices = np.where(dataset.isna())
nan_count = dataset.isna().sum().sum()
dash_indices = np.where(dataset == '-')
dash_count = len(dash_indices[0])

print("Indices of NaN values: ")
print(nan_indices)
print("Total number of NaNs: ")
print("nan_count")
print("Indices of '-' values in the dataset: ")
print(dash_indices)
print("total number of '-' values in the data set: ")
print(dash_count)

############
dataset.mask(dataset == '-', inplpace=True)
dataset = dataset.astype('float64')

nan_indices = np.where(dataset.isna())
nan_count = dataset.isna().sum().sum()

#######
fill_vals= {
    'fixed acidity': 0,
    'volatile acidity': 0,
    'citric acid': 0,
    'residual sugar': 0,
    'chlorides': 0,
    'free sulfur dioxide': 0,
    'total sulfur dioxide': 0,
    'density': 0,
    "pH": 1,
    'sulphates': 1,
    'alcohol': 0
}
dataset.fillna(value=fill_vals, inplace=True)
nan_count = dataset.isna().sum().sum()
print("total number of Nans in the data after the fill")
print(nan_count)
##########

dataset.fillna(method='ffill', inplace=True)
print("values of the data set at index [16,0] before filling", dataset.iloc[16,0])
print("values of the data set at index [17,0] before filling", dataset.iloc[17,0])

##########
dataset.interpolate(method='linear', inplace=True)
print("value of the dataset at index [17,0] after the interpolation is :", dataset.iloc[17,0])

dataset.mask(dataset == '-', inplace=True)
dataset = dataset.astype('float64')
dataset.fillna(method='fill', inplace=True)


#######
file_path = 'noisy-sine.csv'
data = pd.read_csv(file_path)

data.head()
# making specified window sizes
windowSizes = [5, 31, 51]
filteredSignals = {}

for i in windowSizes:
    filteredSignals[i] = data.rolling(window=i, center=True).mean()

# Plotting
plt.figure(figsize=(20, 10))
plt.plot(data, label="Moving Average for Noise Removal", linewidth=1.5, alpha=1)


for i, j in filteredSignals.items():
    plt.plot(j, label=f'Moving Average (Window size={i})')

plt.title('Noisy Signal and Moving Average Filters')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()

###########
dataset = pd.read_csv('ECG-sample.csv')
dataset.columns = ['ECG']

plt.figure(figsize=(8,10))
plt.plot(dataset.index, dataset['ECG'], color='#00008B')

plt.xlim(left=0, right=215)  # Set the x-axis limit to match the image
plt.ylim(bottom=0, top=1)  # Set the y-axis limit to match the image


plt.show()
###########
dataset = pd.read_csv('ECG-sample.csv')
dataset.columns = ['ECG']

# rolling feeatures mean, std, max, and min
window_size = 31
features = dataset['ECG'].rolling(window=window_size).agg(['mean', 'std', 'max', 'min'])

# Dropna function to remove NaN
features.dropna(inplace=True)

print(features)

#######
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


dataset = pd.read_csv('ECG-sample.csv')
dataset.columns = ['ECG']

# rolling feeatures mean, std, max, and min
window_size = 31
features = dataset['ECG'].rolling(window=window_size).agg(['mean', 'std', 'max', 'min'])

# Dropna function to remove NaN
features.dropna(inplace=True)
plt.figure(figsize=(10, 8))
plt.plot(features['std'], color='#00008B')
plt.xlabel('Number of the window')
plt.ylabel('Value of the std')

plt.show()