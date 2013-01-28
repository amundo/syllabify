import json
from collections import Counter

def ngrams(seq, n): 
  return [seq[i:i+n] for i in range(len(seq)-n+1)]

def trigrams(seq): return ngrams(seq,3)

words = json.load(open('hil.json'))

def no_trigram_repeats(word):
  """
  Eliminates things like 'Goooood!'
  """
  repeats = [t for t in trigrams(word) if len(set(t)) == 1]
  return len(repeats) == 0

words = [w for w in words if no_trigram_repeats(w) and len(w) > 3]

open('hil-sample.json','w').write(json.dumps(words, indent=2))
