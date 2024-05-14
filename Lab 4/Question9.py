# Question 9
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
df = pd.read_csv('wineQualityN.csv')
df.drop(df.columns[0], axis=1, inplace=True)

df['quality'] = df['quality'].apply(lambda x: 1 if x>= 8 else 0)
features = df.drop('quality', axis=1)
features = StandardScaler().fit_transform(features)

pca = PCA(n_components=11)
pca_result = pca.fit_transform(features)   

plt.figure(figsize=(8, 6))
plt.scatter(pca_result[df['quality'] == 0, 7], pca_result[df['quality'] == 0, 8], c='pink', label='Low quality')
plt.scatter(pca_result[df['quality'] == 1, 7], pca_result[df['quality'] == 1, 8], c='red', label='High Quality')
plt.title('PCA: Principal Component 8 vs Principal Component 9')
plt.xlabel('Principle Compoment 8')
plt.ylabel('Principle Compoment 9')
plt.legend()
plt.show()
