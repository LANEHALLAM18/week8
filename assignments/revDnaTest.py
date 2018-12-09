#!/usr/bin/env python

# establish the variable which represents the dna data.
# issues the user to enter the dna sequence which is used as input.
dnaSeq = input ("Please input your DNA sequence: ")

#the users sequence will be printed to the screen in all caps no matter the original individual letter case.
dnaSeqUpper = dnaSeq.upper()
print ("The input DNA sequence is:")
print (dnaSeqUpper)

# the above sequence is then reversed and printed to the screen.
dnaSeqUpperRev = dnaSeqUpper[::-1]
print ("The reverse DNA strand is:")
print (dnaSeqUpperRev)

# this loop will print the complement sequence to the reverse DNA strand in one line.
print ("The complement of the reverse DNA strand is:",) 
for i in dnaSeqUpperRev:
	if(i == "A"): print("T", end = "") 
	elif(i == "T"): print("A", end = "")
	elif(i == "C"): print("G", end = "")
	elif(i == "G"): print("C", end = "")
print ("")

# DB: Excellent! Works well, is robust, clean, and well commented.