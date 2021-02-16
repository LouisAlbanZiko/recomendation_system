import os
import ahocorasick

# create automaton with keywords
A = ahocorasick.Automaton()
keywords = ["programming", "algorithm", "developer", "code"]
for idx, key in enumerate(keywords):
	A.add_word(key, (idx, key))
A.make_automaton()

results = {}
for file_name in os.listdir("files"):
	# set all counters to 0
	counters = {}
	for key in keywords:
		counters[key] = 0
	
	# read file
	with open("files/"+file_name, 'r') as reader:
		# for each occurence of a word increment the corresponding counter
		for end_index, (insert_order, original_value) in A.iter(reader.read()):
			counters[original_value] += 1
	# append the counters to results
	results[file_name] = sum(counters.values())

# sort the results
result_sorted = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))

# show the results
print("web_page\t|\tcount")
print("-" * 30)
for key in result_sorted:
	print("{0}\t|\t{1}".format(key, result_sorted[key]))
