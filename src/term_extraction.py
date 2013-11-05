from topia.termextract import extract
extractor = extract.TermExtractor()

with open('./corpus/all3.txt', 'r') as f:
	with open('./data/terms.txt', 'w') as o:
		o.write("Term\tOccurences\tStrength\n")
		for term in sorted(extractor(f.read())):
			o.write("\t".join(map(str, term)) + "\n")
