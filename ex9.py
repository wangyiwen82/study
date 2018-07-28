from sys import argv
script,textfile1,textfile2=argv
t1=open(textfile1,'w')
t2=open(textfile2)
t1.write(t2.read())
t1.close()
