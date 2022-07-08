# Create the following variables:
# n = 2022
# x = math.pi
# save with 5 digits after a dot (import 'math' first!)
# word = "Python"
# polish = "książka"
# Write the variables to a text file "vars.txt", one line for one variable.
# Print the file content on the screen.

#var1
import math
outfile = open('vars.txt', 'w', encoding='utf-8')
x = format(math.pi, ".5f")
n = 2022
word = "Python"
polish = "książka"
outfile.write("{}\n{}\n{}\n{}\n".format(n, x, word, polish))
outfile.close()
with open('vars.txt', 'r', encoding='utf-8') as f:
    print(f.read())

#var2
import math
n = 2022
x = math.pi
word = "Python"
polish = "książka"
with open('vars.txt', 'w') as outfile:
    for item in (n, f"{x:.5f}", word, polish):
        outfile.write("{}\n".format(item))
print("data saved ...")
with open('vars.txt', 'r') as infile:
    print(infile.read())

