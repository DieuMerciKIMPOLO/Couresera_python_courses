import re
lst=list()
u=0
fichier1=open('regex_sum_57350.txt')
fichier2=open('regex_sum_42.txt')
for line in fichier1:
	line=line.rstrip()
	lst+=re.findall('([0-9]+)',line)
for i in lst:
	u+=int(i)
print(u)