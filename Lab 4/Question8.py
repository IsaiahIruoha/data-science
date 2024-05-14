import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('wineQualityN.csv')

df.drop(df.columns[0], axis=1, inplace=True)

df['quality'] = df['quality'].apply(lambda x: 1 if x>= 8 else 0)
features = df.drop('quality', axis=1)
features = StandardScaler().fit_transform(features)

pca = PCA(n_components=2)
pca_result = pca.fit_transform(features)
tsne = TSNE(n_components=2, perplexity=30)
tsne_result = tsne.fit_transform(features)
plt.figure(figsize=(12, 6))

plt.subplot(1,2,1)
plt.scatter(pca_result[df['quality'] == 0, 0], pca_result[df['quality'] == 0, 1], c='pink', label='Low quality')
plt.scatter(pca_result[df['quality'] == 1, 0], pca_result[df['quality'] == 1, 1], c='red', label='High Quality')
plt.title('PCA')
plt.xlabel('Principle Compoment 1')
plt.ylabel('Principle Compoment 2') 
plt.legend()
plt.subplot(1,2,2)
plt.scatter(tsne_result[df['quality'] == 0, 0], tsne_result[df['quality'] == 0, 1], c='pink', label='Low quality')
plt.scatter(tsne_result[df['quality'] == 1, 0], tsne_result[df['quality'] == 1, 1], c='red', label='High Quality')

plt.title('t-SNE')
plt.xlabel('t-SNE Dimension 1')
plt.ylabel('t-SNE Dimension 2')
plt.legend()

plt.tight_layout()
plt.show()