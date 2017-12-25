"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by 
hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the 
time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

name = input("Enter file:")
handle = open(name)
count=dict()
if len(name) < 1 : name = "mbox-short.txt"
for line in handle:
	if line.startswith('From') and not line.startswith('From:'):
		count[line.split()[5].split(':')[0]]=count.get(line.split()[5].split(':')[0],0)+1
for i, j in sorted([(v, w) for v, w in count.items()]):
	print(i,j)