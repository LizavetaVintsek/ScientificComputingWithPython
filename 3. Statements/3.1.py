#For a given word print it in squares.
#var1
line = '+---+---+---+---+'
line1 = '| L | i | z | a |'
L = [line, line1, line]
print('\n'.join(L))
#var1
word = "Amazon"
n = len(word)
line1 = "---".join("+" * (n+1))
line2 = "| " + " | ".join(word) + " |"
#line2 = "|" + "|".join(s.center(3) for s in word) + "|"
#line2 = "|" + "|".join("{:^3}".format(s) for s in word) + "|"
#line2 = "".join("|{:^3}".format(s) for s in word) + "|"
print ("\n".join((line1,line2,line1)))
