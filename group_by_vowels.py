# -*- coding: utf-8 -*-
import re
import sys,codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
import json
from random import choice
from hiligaynon import *

def is_vowel(letter): return set(letter).issubset(set(VOWELS))

def all_vowels(phonemes): return all([is_vowel(letter) for letter in phonemes])

def group_by_vowels(word):
  return [group for group in re.compile(vowelRE).split(word) if group]

def split_by_onsets(consonants):
  """
  we assume (only partially correctly) that consonant sequences
  can be assigned to syllables by finding the longest possible
  suffix which is also a possible onset  
  (The onset list also needs editing, probably)
  """
  onsetRE = re.compile('(wh|tw|tr|th|dy|ty|sy|sw|st|sm|sh|pw|pr|pl|ng|kw|kl|gr|fr|fl|dr|cr|cl|ch|br|z|y|w|v|t|s|r|q|p|n|m|l|k|j|h|g|f|d|c|b)')
  return [group for group in onsetRE.split(consonants) if group]

if __name__ == "__main__":
  sample = set(json.load(sys.stdin))
  for word in sample: 
    #line = line.decode('utf-8')
    #print u'·'.join(group_by_vowels(line))
    groups = []
    for group in  group_by_vowels(word):
      if all_vowels(group):
        groups.append(group)
      else:
        groups.extend(split_by_onsets(group))
    print '|'.join(groups)
    #if not all_vowels(groups[0]): print groups[0]


