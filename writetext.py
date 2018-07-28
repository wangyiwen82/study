from sys import argv
script,textfile=argv
text=open(textfile,'r')
line1="my name is wyw."
line2="i am 20."
line3="i like eating."
line4="abc"
text.write(line1)
text.write("\n")
text.write(line2)
text.write("\n")
text.write(line3)
text.write("\n")
text.write(line4)
text.write("\n")
text.close()
