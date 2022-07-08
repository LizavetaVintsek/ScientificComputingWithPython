#Create a dict for conversion of roman numerals (like I, IV, V, IX, X)
# to arabic numbers. Use different methods.
#var1
numbers = {'I': 1, 'II': 2, 'III': 3, 'IV':4}
print(numbers)
#var2
numbers = [{"arabic": 'I', "roman": 1}, {"arabic": 'II', "roman": 2}, {"arabic": 'III', "roman": 3}, {"arabic": 'IV', "roman": 4}]
print(numbers)
#var3
k = ['I', 'V', 'X', 'L', 'C']
v = [1, 5, 10, 50, 100]
roman = dict(zip(k, v))
print(roman)
#var4
roman2 = dict([('I', 1), ('V', 5), ('X', 10)])
print(roman2)
#var5
roman3 = dict(I=1, V=5, X=10, L=50)
print(roman3)

