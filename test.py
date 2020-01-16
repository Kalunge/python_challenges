a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

b = str(a[:5])
c = str(a[5:])

d = b.replace('(', '')
e = d.replace(')', '')

print(e)

f = c.replace('(', '')
g = f.replace(')', '')

print(g)