from sys import argv
script,first=argv
print "the first is variable is:",first
r=float (first)
def c(a):
    return 2*3.14*a
l=c(r)
if abs(l-40053)<100:
    print "the plant is earth"
elif abs(l-21326)<100:
    print "the plant is mars"
else:
    print "the plant isn't earth or mars"
