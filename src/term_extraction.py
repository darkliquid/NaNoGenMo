from nltk.corpus import gutenberg, abc, reuters, brown, movie_reviews
from topia.termextract import extract
extractor = extract.TermExtractor()

with open('./corpus/all3.txt', 'r') as f:
	with open('./data/terms.txt', 'w') as o:
		o.write("Term\tOccurences\tStrength\n")
		for term in extractor(f.read()+gutenberg.raw()+abc.raw()+reuters.raw()+brown.raw()+movie_reviews.raw()):
			o.write("\t".join(map(str, term)) + "\n")
