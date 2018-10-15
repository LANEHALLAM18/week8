#!/usr/bin/env python

# let user choose an option 
# 1 translate a protein-coding nucleotide sequence to amino acids
# 2 randomly draw a codon from the squence

while True:
	print("")
	print ("Option 1 : Type the number '1' to translate a submitted protein coding sequence into an amino acid.")
	print ("")
	print ("Option 2 :Type the number '2' to randomly draw a codon of the submitted sequence.")
	print ("")
	choice = input ("Please Submit Your Choice Now: ")
	if choice not in ('1', '2'):
		print ("Not an Appropriate Answer")
	else:
		print ("You have chose option : ",(choice))
		print("")
		break

while True:
	print ("Have you chosen the correct option?")
	decision = input(" Choose: [Y] or [N] : ")
	if decision not in ('Y', 'N', 'y', 'n'):
		print ("Not an Appropriate Answer") 
		print ("")
	else:
		break
while True:
	if decision not in ('N','n'): 
		print ("")
		print ("Proceeding....")
		break
	else:quit()

dnaSeq = input ("Please input your DNA sequence: ")
print("")
#the users sequence will be printed to the screen in all caps no matter the original individual letter case.
dnaSeqUpper = dnaSeq.upper()
print ("The input DNA sequence is:",(dnaSeqUpper))
