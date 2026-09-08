def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:

	if not packages:
		return []

	valid_packages: set[str] = set(packages.keys())
	in_degree: dict[str, int] = {}
	adj: dict[str, list[str]] = {pkg: [] for pkg in packages}

	for pkg, deps in packages.items():
		clean_deps = set(dep for dep in deps if dep in valid_packages)

		if pkg in clean_deps:
			return []

		in_degree[pkg] = len(clean_deps)
		for dep in clean_deps:
			adj[dep].append(pkg)

	current_level = [pkg for pkg, deg in in_degree.items() if deg == 0]
	result = []

	while current_level:
		current_level.sort()
		result.extend(current_level)

		next_level = []
		for pkg in current_level:
			for dependent in adj[pkg]:
				in_degree[dependent] -= 1
				if in_degree[dependent] == 0:
					next_level.append(dependent)

		current_level = next_level

	if len(result) != len(packages):
		return []

	return result

if __name__ == "__main__":
	print(package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []}))
	print(package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]}))
	print(package_dependency_resolver({}))
	print(package_dependency_resolver({"X": ["Y"], "Y": ["X"]}))
	print(package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}))
