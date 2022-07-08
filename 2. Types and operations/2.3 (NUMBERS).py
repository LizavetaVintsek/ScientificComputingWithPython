#Find the sum 1*1 + 3*3 + 5*5 + ... + 2021*2021 [hint: use sum()].
x = 1
result = (sum(x*x for x in range(1,2022,2)))
print('sum {}'.format(result))
