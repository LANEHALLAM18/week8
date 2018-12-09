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

#the next two while true statements verify the users choice of options and will end the script if they chose incorrectly.

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

#the user will be asked to enter the dna sequence.

dnaSeq = input ("Please input your DNA sequence: ")
print("")

#the users sequence will be printed to the screen in all caps no matter the original individual letter case.
#the dna strand will be printed in codons.

dnaSeqUpper = dnaSeq.upper()
s = dnaSeqUpper

codonSeq = (" ".join(s[i: i + 3] for i in range(0, len(s), 3)))

#print (codonSeq)
print ("The input DNA sequence is: ",(codonSeq.split()))
print("")
#Rna with spaces
rnaSeq = codonSeq.replace("T", "U")
#Rna with no spaces
rnaSeq2 = s.replace("T", "U")

#if the usr chose option 1 this script print the rna sequence which is need in option one to determine the amino acids.
if choice == "1": print ("RNA Sequence : ",(rnaSeq))
print("")

# setting dictionary for codon to amino acid
codonDict = {"AAA":"Lys", "AAC":"Asn", "AAG":"Lys", "AAU":"Asn", 
		"ACA":"Thr", "ACC":"Thr", "ACG":"Thr", "ACU":"Thr", 
		"AGA":"Arg", "AGC":"Ser", "AGG":"Arg", "AGU":"Ser", 
		"AUA":"Ile", "AUC":"Ile", "AUG":"Met", "AUU":"Ile", 

		"CAA":"Gln", "CAC":"His", "CAG":"Gln", "CAU":"His", 
		"CCA":"Pro", "CCC":"Pro", "CCG":"Pro", "CCU":"Pro", 
		"CGA":"Arg", "CGC":"Arg", "CGG":"Arg", "CGU":"Arg", 
		"CUA":"Leu", "CUC":"Leu", "CUG":"Leu", "CUU":"Leu", 

		"GAA":"Glu", "GAC":"Asp", "GAG":"Glu", "GAU":"Asp", 
		"GCA":"Ala", "GCC":"Ala", "GCG":"Ala", "GCU":"Ala", 
		"GGA":"Gly", "GGC":"Gly", "GGG":"Gly", "GGU":"Gly", 
		"GUA":"Val", "GUC":"Val", "GUG":"Val", "GUU":"Val",
 
		"UAA":"STOP", "UAC":"Tyr", "UAG":"STOP", "UAU":"Thr", 
		"UCA":"Ser", "UCC":"Ser", "UCG":"Ser", "UCU":"Ser", 
		"UGA":"STOP", "UGC":"Cys", "UGG":"Trp", "UGU":"Cys", 
		"UUA":"Leu", "UUC":"Phe", "UUG":"Leu", "UUU":"Phe"}

# translating rna codons to amino acids if usr chose option 1 or picks a random codon if usr chose option 2.
codon = [dnaSeqUpper[i:i+3] for i in range(0, len(dnaSeqUpper), 3)]

if choice == "1":
	proteinSeq = ""
	if len(rnaSeq2)%3 == 0:
		for n in range(0, len(rnaSeq), 3):
			if rnaSeq2[n:n+3] in codonDict:
				proteinSeq += codonDict[rnaSeq2[n:n+3]]
		print("Protein sequence: ",(proteinSeq))
		print("")
		print("Your Test is Done!")
		
else:
	import random
	randomCodon = random.choice(codon)
	print("Your Random Codon: ",(randomCodon))
	print("")
	print("Your Test is Done!")

# DB: Why are these lines down here? They don't seem to do anything meaningful.
dnaSeqUpper = dnaSeq.upper()
s = dnaSeqUpper
codonSeq = (" ".join(s[i: i + 3] for i in range(0, len(s), 3)))
codon = [dnaSeqUpper[i:i+3] for i in range(0, len(dnaSeqUpper), 3)]
quit()

# DB: Overall, very well done again. Everything works, is well commented, and well organized.
#     I also like the user checks and dummyproofing that you included. The only comments I
#     have are that there seems to be some leftover code at the bottom, and the structure
#     could be improved a bit if you just used a single if...else statement for choices 1
#     and 2. You could include all the relevant code for translation in the if section.

