#include <stdmap.pbi>
#include <format.pbi>
#include "helpers.pbi"
#include "cities.pbi"
#include "names.pbi"
#include "words.pbi"
#include "title.pbi"

%resource organisation: "The Company";

#include "sentences.pbi"

S:	
	//PROLOGUE TITLE(title>upcase-first)
	//BODY
	//{ chapcount = 0 }
	chapters "\n\n"
	//EPILOGUE
;

chapter:
	//{ chapcount = chapcount + 1 }
	//"Chapter " $chapcount ": " title "\n\n"
	paragraphs
;

chapters: 
	chapters chapter 
	| chapters chapter
	| chapters chapter
	| chapters chapter
	| chapters chapter
	| chapters chapter
	| chapters chapter
	| chapters chapter
	| chapter 
;

paragraphs: 
	intro-paragraph "\n\n" paragraphs-2
;

paragraphs-2: 
	paragraphs "\n\n" paragraph 
	| paragraphs "\n\n" paragraph 
	| paragraphs "\n\n" paragraph
	| paragraphs "\n\n" paragraph 
	| paragraphs "\n\n" paragraph
	| paragraphs "\n\n" paragraph 
	| paragraphs "\n\n" paragraph
	| paragraphs "\n\n" paragraph 
	| paragraph "\n\n" paragraph "\n\n" paragraph
	| paragraph "\n\n" paragraph 
;

intro-paragraph: 
	sentence paragraph
;

paragraph: 
	sentence sentence sentence sentence sentence
;