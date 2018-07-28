vlist=['a','b','c']
vtuple=('a','b','c')
vdict={'a': 1, 'b': 2, 'c': 3}
vset={'a','b','c'}
vstr='abc'
for x in vlist:
    print('list:',x)
for x in vtuple:
    print('tuple:',x)
for x in vdict:
    print('dict:',x)
for x in vset:
    print('set:',x)
for x in vstr:
    print('str:',x)

x=0.0 
for i in range (1,11,1):
    x=x+i*i
    print x
