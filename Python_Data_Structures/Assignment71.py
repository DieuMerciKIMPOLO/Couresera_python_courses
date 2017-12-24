# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for fichier in fh:
    fichier=fichier.rstrip()
    print(fichier.upper())
#print(fh.read().upper())