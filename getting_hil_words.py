import sys,codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
import json
import nltk
import re
print 'do not use this ' 
exit()
wicked = json.load(open('wickedCorpus.json'))

eng =[w.strip().lower() for w in  open('/usr/share/dict/words').read().decode('utf-8').splitlines()]
eng2 = eng[:]
[eng.append(w + 's') for w in eng2]

hil = [w for w in wicked if w.lower() not in eng]
hil = json.load(open("hil.json"))
text = u''

for v in wicked.values(): 
  text +=  ' '.join(v)

#text = re.sub('\.\.[\.]+', '', text)
text = re.sub('\.[\.]+', '. ' , text)
text = re.sub('\.[\\]+', ' ' , text)

sentences = nltk.sent_tokenize(text)
words = []
[words.extend(nltk.word_tokenize(sent)) for sent in sentences]

words = [ w for w in words if set(w).intersection(set(u'aeiouáéíóú'))]

vocab = set(words)
engvocab = set(eng)

hil = [w for w in words if w.lower() not in engvocab]
print '\n'.join(hil)

open('hil.json','w').write(json.dumps(hil, indent=2))
open('hil.txt','w').write('\n'.join(hil).encode('utf-8'))
