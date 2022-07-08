#Let S be a long string (many lines).
S = "Unicode is an encoding for\ntextual characters which is able to represent\ncharacters from many different languages\nfrom around the world."
print (S)
#1.Find the number of black characters in S [not whitespace, see the method S.isspace()].
#var1
SplitString = str.split(S)
print (len(SplitString))
#var2
L = S.split()
print (len(L))
#2.Find the number of words in S (a word is a sequence of black characters).
#var1
print (S.count(" ")+1)
#var2
print (len(set(L)))
#3.Find the longest word in S.
#var1
print (max(SplitString, key=len))
#var2
print (max(L, key=len))
#4.Sort words from S according to the lexicographic order.
#var1
print (sorted(SplitString))
#var2
print (sorted(L))
#5.Sort words from S according to the the length.
#var1
print (sorted(SplitString, key=len))
#var2
print (sorted(L, key=len))
#6.Find number of letters in S.
#var1
print (sum(len(word) for word in L))
#var2
print (sum(1 for char in S if not char.isspace()))

