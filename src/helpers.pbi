// Functions
double-around(foo bar): foo bar foo ;
interleave-two-with-one(foo bar baz): foo baz bar baz ;

// Numbers
%resource non-zero-digit: "1"|"2"|"3"|"4"|"5"|"6"|"7"|"8"|"9";
%resource digit: "0"|non-zero-digit;

// Letters
%resource consonant: "b" | "c" | "d" | "f" | "g" | "h" | "j" | "k" | "l" | "m" | "n" | "p" | "q" | "r" | "s" | "t" | "v" | "w" | "x" | "y" | "z" | "w" | "w" | "w" | "qu";
%resource vowel: "a" | "e" | "i" | "o" | "u" | "ea" | "ee" | "oo" | "ar" | "or" ;
%resource sibilant-bit: sibilant-cons | sibilant-cons post-sibilant ;
%resource post-sibilant: "l" | "n" ;
%resource sibilant-cons: "f" | "ph" | "s" | "sh" | "sch" | "x" | "z";
%resource plosive-cons: plosive-cons-a | plosive-cons-b ;
%resource plosive-cons-a: "b" | "d" | "p" ;
%resource plosive-cons-b: "t" | "k" | "ck" ;

%resource syllable: consonant vowel sibilant-cons
        | sibilant-bit vowel plosive-cons
        | consonant vowel plosive-cons-a plosive-cons-a
        | double-around(consonant vowel)
        | double-around(consonant "oo")
        | sibilant-bit vowel sibilant-cons plosive-cons-b
        | interleave-two-with-one(consonant consonant vowel)
;
%resource random-word: syllable | double-around(syllable vowel);

pluralise:
	".*y$" -> "y$"/"ies"
	".*s$" -> "$"/"es"
	".*" -> "$"/"s"
;

ordinalise:
	".*1$" -> "1$"/"1st"
	".*2$" -> "2$"/"2nd"
	".*3$" -> "3$"/"3rd"
	".*4$" -> "4$"/"4th"
	".*5$" -> "5$"/"5th"
	".*6$" -> "6$"/"6th"
	".*7$" -> "7$"/"7th"
	".*8$" -> "8$"/"8th"
	".*9$" -> "9$"/"9th"
	".*0$" -> "0$"/"0th"
;

