import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample vectors
vector1 = np.array([1, 2, 3])
vector2 = np.array([3, 4, 5])

# Reshape the vectors to be 2D arrays (required by cosine_similarity)
vector1 = vector1.reshape(1, -1)
vector2 = vector2.reshape(1, -1)

# Calculate cosine similarity
similarity = cosine_similarity(vector1, vector2)

print("Cosine Similarity:", similarity[0][0])
