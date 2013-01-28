def longest_suffix_match(word, suffixes):
  suffixes = sorted(suffixes, key=len, reverse=True)
  for suffix in suffixes: 
    if word.endswith(suffix):
      return word[:-len(suffix)], suffix
  return word

suffixes = 'CV CVC V'.split()
print longest_suffix_match('CVCVC', suffixes)


    
