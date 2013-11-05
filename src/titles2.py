from textblob import TextBlob
from textblob_aptagger import PerceptronTagger
from random import choice
import string
import gzip

txt = gzip.open("corpus/titles.txt.gz",'r').read()
blob = TextBlob(filter(lambda x: x in string.printable, txt), pos_tagger=PerceptronTagger())

with open('./data/title_structures.txt', 'w') as f:
	processed_count = 0
	print "Adding title structures ({0})...".format(len(blob.sentences))
	for sentence in blob.sentences:
		processed_count += 1
		try:
			tags = [tag[1] for tag in sentence.tags]
			if(len(tags) < 8):
				f.write(" ".join(tags) + "\n")
			del sentence
		except:
			print "\r",
		print "Processed {0} sentences\r".format(processed_count),
	del blob