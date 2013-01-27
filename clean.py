import json
import string
alphabet = string.ascii_letters + '-'
words = json.load(open('hil.json'))
words = [w for w in words if set(w).issubset(set(alphabet))]
open('hil2.json','w').write(json.dumps(words, indent=2))

