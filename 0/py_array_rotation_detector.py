def array_rotation_detector(arr1: list, arr2: list) -> bool:

	return sorted(arr1) == sorted(arr2)

if __name__ == "__main__":
	print(array_rotation_detector([1, 2, 3, 4, 5, 8], [4, 5, 1, 2, 3]))
	print(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))
	print(array_rotation_detector([], []))
