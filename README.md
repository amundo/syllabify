syllabifier
-----------

This is an (in-progress!) attempt at a very simple syllabification algorithm.

I'm designing it for use on Hiligaynon, an Austronesian language with a pretty
simple syllable structure, with a pretty shallow orthography. For other
situations, YMMV.

It goes like this:

Get a bunch of words.

Define any digraphs or trigraphs, and split the word into a list of graphemes. 
(ng is a digraph here).

> ilonggo -> i|l|o|ng|g|o
> halong -> h|a|l|o|ng

Make a list of everything-up-to-the-first-vowel in each word. These are the 
canonical onsets.

So if the list of words is halong, kadto, braso, you end up with the list: 
h, k, br. 

Split the word into vowel sequences and consonant sequences:

> ilonggo -> i-l-o-ng|g-o
> halong -> h-a-l-o-ng

Note that this is subtly different from splitting into graphemes.

Now, we make the (not terribly sound) assumption that word-initial onsets 
suffice to define all syllable-initial onsets, and use this to split 
consonantal sequences, in the following way: 

Split consonantal sequences on the list of canonical onsets.

Now we have a list of segments that can be easily classified as C or V. 
By starting with an exhaustive list of possible syllable schema in the
language in question, we can assign syllable breaks back into the original
word. Here's the whole procedure:

> ‘Ilonggo’
> ilonggo
> i|l|o|ng|g|o
> i-l-o-ng|g-o
> i-l-o-ng-g-o
> 
> i 	V
> l	C
> o	V
> ng	C
> g	C
> o	V
 
or:

> VCVCCV

We look this up in the list, and see that the syllabification goes:

> V-CVC-CV

And use this information to index back into the segments we started with:

> i.long.go



