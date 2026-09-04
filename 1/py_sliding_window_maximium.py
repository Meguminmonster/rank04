def sliding_window_maximium(nums: list[int], k: int) -> list[int]:
	if not nums or k <= 0:
		return []

	q: list[int] = []
	head: int = 0
	result: list[int] = []

	for i in range(len(nums)):
		if head < len(q) and q[head] <= i - k:
			head += 1
		while len(q) > head and nums[q[-1]] <= nums[i]:
			q.pop()
		q.append(i)
		if i >= k - 1:
			result.append(nums[q[head]])
	return result

if __name__ == "__main__":
	print(sliding_window_maximium([1, 3, -1, -3, 5, 3, 6, 7], 3))
	print(sliding_window_maximium([4, 2, 12, 11, -5], 2))
	print(sliding_window_maximium([], 3))
