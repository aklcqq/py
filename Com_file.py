# This file is for combining the lines
fh = open('test0.txt','r')
fh1 = open('allso.txt','r')
c = ''
nf = open('all.txt', 'a')
a = []
for line in fh:
    a.append(line)
b = []
for line in fh1:
    b.append(line)

print(len(a),len(b))

if len(a) == len(b):
    i = 0
    while i =< int(len(a)):
        c = b[i] + a[i]
        i += 1
        nf.write(c)
    nf.close()
