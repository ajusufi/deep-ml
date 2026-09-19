def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	import numpy as np

	vectors = np.array(vectors)
	cov_matrix = np.cov(vectors)

	return cov_matrix