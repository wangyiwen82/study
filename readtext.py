from sys import argv
scipt,textfile=argv
#textfile=raw_input()
text=open(textfile)
print "the content of %s."%textfile
print text.read()
