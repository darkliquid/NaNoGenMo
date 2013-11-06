#include <stdmap.pbi>
#include <format.pbi>
#include "helpers.pbi"
#include "cities.pbi"
#include "names.pbi"
#include "words.pbi"
#include "title.pbi"

%resource organisation: "The Company";

#include "sentences.pbi"

S: 	PROLOGUE TITLE(title>upcase-first)
	BODY
	paragraph+
	EPILOGUE
;

paragraph: sentence+ PBRK;