"""
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent 
the greatest number of mail messages. The program looks for 'From ' lines and takes the second word 
of those lines as the person who sent the mail. The program creates a Python dictionary that maps
 the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, 
the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
bigcount=None
bigword=None
count=dict()
for line in handle:
    if line.startswith('From') and not line.startswith('From:'):
        count[line.split()[1]]=count.get(line.split()[1],0)+1
        
for words, counts in count.items():
    if bigcount is None or counts>bigcount:
        bigword=words
        bigcount=counts
print(bigword, bigcount)