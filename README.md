# NaNoGenMo

My entry for NaNoGenMo. Currently investigating various methods of analysis on
corpus text in order to come up with some kind of engine for generating a few
different kinds of sequences. Thinking about this in layers, I'm trying to split
up generation into several different phases, from individual sentences to
high-level plot themeatics.

I'm looking at hand-building some generators based of rules from various story-
telling and roleplaying games such as [FATE][1], [Fiasco][2] and [Microscope][3], then 
combining those with stuff derived from the corpus text analysis.

None of this is likely to end well.

# Corpus

I'm making use of a few hand-picked novels from Project Gutenburg, namely:

 * http://www.gutenberg.org/1/6/6/1661/
 * http://www.gutenberg.org/2/8/5/2852/
 * http://www.gutenberg.org/8/0/8/8086/
 * http://www.gutenberg.org/6/64/
 * http://www.gutenberg.org/3/2/3/2/32325/
 * http://www.gutenberg.org/8/3/834/
 * http://www.gutenberg.org/6/62/
 * http://www.gutenberg.org/2/0/9/2097/
 * http://www.gutenberg.org/2/4/244/

From which I stripped the non-novel text out to make processing easier.

I'm also using various corpora from the NLTK project, namely gutenberg, abc, 
reuters, brown and movie_reviews as well as a lovecraft corpus found here:
https://raw.github.com/jiko/lovecraft_ebooks/master/corpus.txt

[1]:http://fate-srd.com/
[2]:http://www.bullypulpitgames.com/games/fiasco/
[3]:http://www.lamemage.com/microscope/

# Resources

So far, to generate the various data I'm using, I've grabbed databases and
lists from a variety of sources. The current list includes:

**Names**
http://stackoverflow.com/questions/1803628/raw-list-of-person-names

**Titles**
http://www.gutenberg.org/dirs/GUTINDEX.ALL

**US Cities**
http://wiki.skullsecurity.org/images/5/54/US_Cities.txt

**Job Titles**
http://www.bls.gov/soc/soc_2010_direct_match_title_file.xls

**Adjectives**
http://www.enchantedlearning.com/wordlist/adjectives.shtml

**Nouns**
http://www.momswhothink.com/reading/list-of-nouns.html

# Tools

**The Dada Engine**
http://dev.null.org/dadaengine/