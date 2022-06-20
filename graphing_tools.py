# Automate generation of a histogram
def state_histogram(states, buckets):
import matplotlib.pyplot as plt

	fig, ax = plt.subplots()

	xpos = list(range(len(states)))

	ax.bar(xpos, buckets, alpha=0.4)
	ax.set_xticks(xpos)
	ax.set_xticklabels(states)
	ax.yaxis.grid(True)
	ax.set_xlabel("State")
	ax.set_ylabel("Probability")

	plt.show()

# Generate the input lists for our histogram function from a braket counts object.
def braket_unpack(counts):
	raw_states = counts.keys()
	states = []
	buckets = []
	nsamples = 0
	for a in raw_states:
		nsamples += counts[a]
		states.append("|"+a+">")
	for a in raw_states:
		buckets.append(counts[a]/nsamples)        
	return states,buckets


# Generate the input lists for our histogram function from a MyQLM results object.
def myqlm_unpack(result):
	buckets = []
	states = []
	for sample in result:
		buckets.append(sample.probability)
		states.append(sample.state)
	return states,buckets   
