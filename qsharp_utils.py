# Here are some utilities to make Q# more usable:

# Returns a dict of states
def MultiSim(c, n):
	results = {}
	for a in range(n):
		r = c.simulate()
		key = ""
		for b in r:
			key = key + str(b)
		if key in results:
			results[key] = results[key] + 1
		else:
			results[key] = 1
	return results
