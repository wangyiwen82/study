def earth(a):
    return 2*a*3.14
def mars(b):
    return 2*b*3.14
r1=6378
r2=3396
e=earth(r1)
print "the circumference of the earth.",float(e)
m=mars(r2)
print "the circumference of the mars.",float(m)
