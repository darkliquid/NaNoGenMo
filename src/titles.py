import re

with open('./corpus/titles.txt', 'w') as o:
	with open("./corpus/GUTINDEX.ALL.txt",'r') as f:
		for line in f.readlines():
			match = re.search(r"(.*), [Bb]y.*\d+[a-zA-Z]?$", line.strip())
			if match:
				print match.group(1).strip()
				o.write(match.group(1).strip()+"\n")
			else:
				print "Failed:" + line.strip()