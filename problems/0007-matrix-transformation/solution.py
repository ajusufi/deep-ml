import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	
	inverse_T = 0
	inverse_S = 0

	try:
		inverse_T = np.linalg.inv(T)
		inverse_S = np.linalg.inv(S)
	except:
		return -1

	return inverse_T @ A @ S
