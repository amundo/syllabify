# -*- coding: utf-8 -*-
import re

SYLLABLEPATTERNS = """
V
CV
CVC

CVCV
CVCVC
CVCCV
CVCCVC

CVCVCV
CVCVCVC
CVCVCCV
CVCVCCVC

CVCCVCV
CVCCVCVC
CVCCVCCV
CVCCVCCVC

CVCVCCVCV
CVCVCCVCVC
CVCVCCVCCV
CVCVCCVCCVC

CVCCVCCVCV
CVCCVCCVCVC
CVCCVCCVCCV
CVCCVCCVCCVC
""".strip().split()

syllableRE = re.compile('(CVC|CV|V)+')

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

