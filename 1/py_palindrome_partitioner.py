def palindrome_partitioner(s: str) -> int:
	n = len(s)
	if n <= 1:
		return 0

	dp = [i - 1 for i in range(n + 1)]

	for center in range(n):
		left, right = center, center
		while left >= 0 and right < n and s[left] == s[right]:
			dp[right + 1] = min(dp[right + 1], dp[left] + 1)
			left -= 1
			right += 1

		left, right = center, center + 1
		while left >= 0 and right < n and s[left] == s[right]:
			dp[right + 1] = min(dp[right + 1], dp[left] + 1)
			left -= 1
			right += 1

	return dp[n]

if __name__ == "__main__":
	print(palindrome_partitioner("aab"))
	print(palindrome_partitioner("aba"))
	print(palindrome_partitioner("abc"))
