def coins(coins, change):
	"""Returns combination of coins given a list of denominations and change amount."""

	combination = []
	i = 0

	for i in range(len(coins) - 1):
		counter = 0
		while change > coins[i] and change - coins[i] > coins[-1]:
			change -= coins[i]
			counter += 1
		combination.append(counter)
		i += 1

	combination.append(change / coins[-1])

	return combination