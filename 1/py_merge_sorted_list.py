def merge_two_lists(l1: list[int], l2: list[int]) -> list[int]:

	result = []
	i, j = 0, 0

	while i < len(l1) and j < len(l2):
		if l1[i] <= l2[j]:
			result.append(l1[i])
			i += 1
		else:
			result.append(l2[j])
			j += 1
	while i < len(l1):
		result.append(l1[i])
		i += 1
	while j < len(l2):
		result.append(l2[j])
		j += 1

	return result

def merge_sorted_list(lists: list[list[int]]) -> list[int]:

	if not lists:
		return []

	merged_lists = lists

	while len(merged_lists) > 1:
		next_level = []
		for idx in range(0, len(merged_lists), 2):
			if idx + 1 < len(merged_lists):
				merged = merge_two_lists(merged_lists[idx], merged_lists[idx + 1])
				next_level.append(merged)
			else:
				next_level.append(merged_lists[idx])
		merged_lists = next_level

	return merged_lists[0] if merged_lists else []

if __name__ == "__main__":
	print(merge_sorted_list([[1, 4, 5], [1, 3, 4], [2, 6]]))
	print(merge_sorted_list([[1, 2, 3], [], [0, 4]]))
	print(merge_sorted_list([]))
	print(merge_sorted_list([[], []]))
