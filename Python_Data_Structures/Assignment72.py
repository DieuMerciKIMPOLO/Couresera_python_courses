# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
nombre=0.0
nbre=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
    	try:
    		text = line
    		text_number=text.find(" ")
    		F=float(text[text_number+1: len(text)])
    		nombre+=F 
    		nbre=nbre+1
    	except:
    		continue
print("Average spam confidence:", float(nombre/nbre))