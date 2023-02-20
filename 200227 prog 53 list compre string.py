
sent = 'comprehension'

t1 = [c for c in sent if c not in 'AEIOU' + 'aeiou']

t = "".join( [c for c in sent if c not in 'AEIOU' + 'aeiou'])

#t = "".join( [c for c in sent ])

print(t1)
print(t)
