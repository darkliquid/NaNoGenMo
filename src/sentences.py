with open('./average_length_structures.txt', 'w') as o:
	with open("./sentence_structures.txt",'r') as f:
		for line in f:
			word_count = len(line.split(' '))
			# Average sentence length according to Oxford Guide To Plain English
			if word_count >= 15 and word_count <= 20:
				o.write(line)