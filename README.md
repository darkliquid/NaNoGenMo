# NaNoGenMo

My entry for NaNoGenMo. Currently investigating various methods of analysis on
corpus text in order to come up with some kind of engine for generating a few
different kinds of sequences. Thinking about this in layers, I'm trying to split
up generation into several different phases, from individual sentences to
high-level plot themeatics.

I'm looking at hand-building some generators based of rules from various story-
telling and roleplaying games such as FATE, Fiasco and Microscope, then 
combining those with stuff derived from the corpus text analysis.

None of this is likely to end well.

# Corpus

I'm making use of a few hand-picked novels from Project Gutenburg, namely:

http://www.gutenberg.org/1/6/6/1661/
http://www.gutenberg.org/2/8/5/2852/
http://www.gutenberg.org/8/0/8/8086/
http://www.gutenberg.org/6/64/
http://www.gutenberg.org/3/2/3/2/32325/
http://www.gutenberg.org/8/3/834/
http://www.gutenberg.org/6/62/
http://www.gutenberg.org/2/0/9/2097/
http://www.gutenberg.org/2/4/244/

Which have the non-novel text stripped out to make processing easier.

I'm also using various corpora from the NLTK project, namely gutenberg, abc, 
reuters, brown and movie_reviews.