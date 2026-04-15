import numpy as np
from sklearn.decomposition import PCA

def get_embeddings(words):
    # Simulación simple (puedes conectar OpenAI o HF)
    return np.random.rand(len(words), 50)

def reduce_dimensionality(vectors):
    pca = PCA(n_components=2)
    return pca.fit_transform(vectors)