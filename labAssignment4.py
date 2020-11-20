#!/usr/bin/env python

file = open("sequence.fasta")
lines = file.readlines()
sequence = []
for i in range(1,len(lines)-1):
	sequence.append(lines[i].strip("\n"))
sequence = "".join(sequence)

print "Here is the sequence: "
print sequence + "\n"

pt1,pt2 = sequence.split("CCCGGG")

print "Here is the sequence split in half: "
print "pt1: "
print pt1 + "\n"
print pt2 + "\n"

file = open("insert.fasta")
newLine = file.readlines()
newText = newLine[1].strip().lower()
print "Here is the newly inserted line: "
print newText + "\n"

newSequence = pt1 + "CCC" + newText + "GGG" + pt2
print "Here is the newly combined sequence: "
print newSequence +  "\n"

f = open("output.txt","w+")

f.write(">puc19c SmaI insert.fasta\n")
f.write(newSequence)
f.close()
file.close()

