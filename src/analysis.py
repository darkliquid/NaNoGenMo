from textblob import TextBlob
from textblob_aptagger import PerceptronTagger
from sets import Set
from nltk.corpus import gutenberg, abc, reuters, brown, movie_reviews
import string

# Reference
tag_types = {
	'CC': 	'Coordinating conjunction',
	'CD': 	'Cardinal number',
	'DT': 	'Determiner',
	'EX': 	'Existential there',
	'FW': 	'Foreign word',
	'IN': 	'Preposition or subordinating conjunction',
	'JJ': 	'Adjective',
	'JJR': 	'Adjective, comparative',
	'JJS': 	'Adjective, superlative',
	'LS': 	'List item marker',
	'MD': 	'Modal',
	'NN': 	'Noun, singular or mass',
	'NNS': 	'Noun, plural',
	'NNP': 	'Proper noun, singular',
	'NNPS': 'Proper noun, plural',
	'PDT': 	'Predeterminer',
	'POS': 	'Possessive ending',
	'PRP': 	'Personal pronoun',
	'PRP$': 'Possessive pronoun',
	'RB': 	'Adverb',
	'RBR': 	'Adverb, comparative',
	'RBS': 	'Adverb, superlative',
	'RP': 	'Particle',
	'SYM': 	'Symbol',
	'TO': 	'to',
	'UH': 	'Interjection',
	'VB': 	'Verb, base form',
	'VBD': 	'Verb, past tense',
	'VBG': 	'Verb, gerund or present participle',
	'VBN': 	'Verb, past participle',
	'VBP': 	'Verb, non-3rd person singular present',
	'VBZ': 	'Verb, 3rd person singular present',
	'WDT': 	'Wh-determiner',
	'WP': 	'Wh-pronoun',
	'WP$': 	'Possessive wh-pronoun',
	'WRB': 	'Wh-adverb'
}

type_words = {}
sentences = Set()
processed_count = 0

print "Loading Corpus Text..."
txt = open("corpus/all3.txt",'r')
blob = TextBlob(txt.read(), pos_tagger=PerceptronTagger())
txt.close()

print "Adding corpus sentence structures ({0})...".format(len(blob.sentences))
for sentence in blob.sentences:
	processed_count += 1
	try:
		tags = tuple([tag[1] for tag in sentence.tags])
		sentences.add(tags)
		del sentence
	except:
		print "\r",
	print "Processed {0} sentences\r".format(processed_count),
print "Current Structure total: {0}".format(len(sentences))
del blob

print "Adding gutenberg sentence structures ({0}) ...".format(len(gutenberg.sents()))
for sentence in gutenberg.sents():
	processed_count += 1
	try:
		blob = TextBlob(filter(lambda x: x in string.printable, " ".join(sentence)), pos_tagger=PerceptronTagger())
		tags = tuple([tag[1] for tag in blob.tags])
		sentences.add(tags)
	except:
		print "\r",
	print "Processed {0} sentences\r".format(processed_count),
print "Current Structure total: {0}".format(len(sentences))

print "Adding abc sentence structures ({0})...".format(len(abc.sents()))
for sentence in abc.sents():
	processed_count += 1
	try:
		blob = TextBlob(filter(lambda x: x in string.printable, " ".join(sentence)), pos_tagger=PerceptronTagger())
		tags = tuple([tag[1] for tag in blob.tags])
		sentences.add(tags)
	except:
		print "\r",
	print "Processed {0} sentences\r".format(processed_count),
print "Current Structure total: {0}".format(len(sentences))

print "Adding reuters sentence structures ({0})...".format(len(reuters.sents()))
for sentence in reuters.sents():
	processed_count += 1
	try:
		blob = TextBlob(filter(lambda x: x in string.printable, " ".join(sentence)), pos_tagger=PerceptronTagger())
		tags = tuple([tag[1] for tag in blob.tags])
		sentences.add(tags)
	except:
		print "\r",
	print "Processed {0} sentences\r".format(processed_count),
print "Current Structure total: {0}".format(len(sentences))

print "Adding brown sentence structures ({0})...".format(len(brown.sents()))
for sentence in brown.sents():
	processed_count += 1
	try:
		blob = TextBlob(filter(lambda x: x in string.printable, " ".join(sentence)), pos_tagger=PerceptronTagger())
		tags = tuple([tag[1] for tag in blob.tags])
		sentences.add(tags)
	except:
		print "\r",
	print "Processed {0} sentences\r".format(processed_count),
print "Current Structure total: {0}".format(len(sentences))

print "Adding movie_review sentence structures ({0})...".format(len(movie_reviews.sents()))
for sentence in movie_reviews.sents():
	processed_count += 1
	try:
		blob = TextBlob(filter(lambda x: x in string.printable, " ".join(sentence)), pos_tagger=PerceptronTagger())
		tags = tuple([tag[1] for tag in blob.tags])
		sentences.add(tags)
	except:
		print "\r",
	print "Processed {0} sentences\r".format(processed_count),

print "Processed {0} sentences".format(processed_count)
print "Current Structure total: {0}".format(len(sentences))

print "Saving structures to text file"
f = open('./sentence_structures.txt', 'w')
for sentence in sentences:
	f.write(" ".join(sentence))
	f.write("\n")
f.close()
