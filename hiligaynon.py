# -*- coding: utf-8 -*-
import re

SYLLABLEPATTERNS = """
CV
CVC
CVCV
CVCCV
CVCCVC
""".strip().split()

VOWELS = u'áéíóúaeiouàèìòùÁÉÍÓÚAEIOUÀÈÌÒÙ'
vowelRE = u'([' + VOWELS + '])'

ONSETS = """wh
tw
tr
th
dy
ty
sy
ry
sw
st
sm
sh
pw
pr
pl
ng
kw
kl
gr
fr
fl
dr
cr
cl
ch
br
z
y
w
v
t
s
r
q
p
n
m
l
k
j
h
g
f
d
c
b
-""".strip().split()

onsetRE = re.compile( u'(' + '|'.join(ONSETS) + ')' )

