#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys,codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
import json
from random import choice
from hiligaynon import *
import itertools

syllables = 'CV CVC'.split()
schemas = [] 
for i in 2, 3:
 for schema in  list(itertools.product(syllables, repeat=i)): 
  schemas.append(''.join(schema))
  schemas.append('V' + ''.join(schema))

def is_vowel(letter): 
  return set(letter).issubset(set(VOWELS))

def all_vowels(phonemes): 
  return all([is_vowel(letter) for letter in phonemes])

def segment_by_vowels(word):
  return [segment for segment in re.compile(vowelRE).split(word) if segment]

def split_by_onsets(consonants):
  """
  we assume (only partially correctly) that consonant sequences
  can be assigned to syllables by finding the longest possible
  suffix which is also a possible onset  
  (The onset list also needs editing, probably)
  """
  return [segment for segment in onsetRE.split(consonants) if segment]

def segmentize(word):
  segments = []
  for segment in  segment_by_vowels(word):
    if all_vowels(segment):
      segments.append(segment)
    else:
      segments.extend(split_by_onsets(segment))
  return segments

def schematize(segments):
  schema = ''
  for s in segments:
    if all_vowels(s): schema += 'V'
    else: schema += 'C'
  return schema

def syllabify(word):
  schema = schematize(segmentize(word))

if __name__ == "__main__":
  from collections import defaultdict
  match = defaultdict(list)
  sample = set(json.load(sys.stdin))
  for word in sample: 
    segments = segmentize(word)
    cv = schematize(segments)
    match[cv].append( word )
  for cv, matches in match.items():
    if cv in schemas:
      match.pop(cv)
      print cv
      print word
      print ', '.join(matches)
      print

