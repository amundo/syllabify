import itertools
alphabet = ['A','B','C','D']
combos = itertools.combinations(alphabet, 3)
print list(combos)
syllables = 'V CV CVC'.split()
print list(itertools.combinations(syllables, 5))
print list(itertools.combinations(syllables, 3))
print list(itertools.product(syllables, repeat=2))
print list(itertools.product(syllables, repeat=3))
for schema in  list(itertools.product(syllables, repeat=3)): print ''.join(schema)
syllables = 'CV CVC'.split()
for schema in  list(itertools.product(syllables, repeat=3)): print ''.join(schema)
for i in 2, 3:
 print i
for i in 2, 3:
 for schema in  list(itertools.product(syllables, repeat=i)): print ''.join(schema)
schemas = [] 
for i in 2, 3:
 for schema in  list(itertools.product(syllables, repeat=i)): schemas.append(''.join(schema))
schemas = [] 
for i in 2, 3:
 for schema in  list(itertools.product(syllables, repeat=i)): 
  schemas.append(''.join(schema))
  schemas.append('V' + ''.join(schema))
schemas
print '\n'.join(schemas)
readline.write_history_file('generate_schemas.py')
