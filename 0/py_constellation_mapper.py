def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:

	grid = [["." for _ in range(size)] for _ in range(size)]

	for r, c in stars:
		if 0 <= r < size and 0 <= c < size:
			grid[r][c] = "*"

	return ["".join(row) for row in grid]

if __name__ == "__main__":
	print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))
	print(constellation_mapper([(0, 0), (0, 1), (0, 2), (1, 1), (2, 2)], 3))
	print(constellation_mapper([(0, 0), (5, 5), (2, 2)], 3))
	print(constellation_mapper([(0, 0), (5, 5)], 2))
