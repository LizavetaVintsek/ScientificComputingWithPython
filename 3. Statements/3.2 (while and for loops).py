#Make a loop over integer numbers from 1 to 40.
#If x is divided by 5 then print a message 'x is divided by 5'.
#If x is divided by 7 then print a message 'x is divided by 7'.
#If x is divided by 5 and 7 then print a message 'x is divided by 5 and 7'.
#Skip x = 13.
#If x is not divided by 5 and x is not divided by 7
#then print a message 'x is not important'.
#Prepare two solutions with 'while' and 'for' loops

#while loop
#var1
n = 1
while n < 41:
    if n == 13:
        n = n + 1
        continue
    if (n % 5) == 0 and (n % 7) == 0:
        print('{} is divided by 5 and 7'.format(n))
    elif (n % 5) == 0:
        print('{} is divided by 5'.format(n))
    elif (n % 7) == 0:
        print('{} is divided by 7'.format(n))
    else:
        print('{} is not important'.format(n))
    n = n + 1
#var2
n = 41
while n > 1:
    n = n - 1
    if n == 13:
        continue
    if (n % 5) == 0 and (n % 7) == 0:
        print(str(n) + ' is divided by 5 and 7')
    elif (n % 5) == 0:
        print(str(n) + ' is divided by 5')
    elif (n % 7) == 0:
        print(str(n) + ' is divided by 7')
    else:
        print(str(n) + ' is not important')

#for loop
#var1
for n in range(0, 40):
    n = n + 1
    if n == 13:
        continue
    if (n % 5) == 0 and (n % 7) == 0:
        print(str(n) + ' is divided by 5 and 7')
    elif (n % 5) == 0:
        print(str(n) + ' is divided by 5')
    elif (n % 7) == 0:
        print(str(n) + ' is divided by 7')
    else:
        print(str(n) + ' is not important')
#var2
for n in range(1, 41):
    if n == 13:
        continue
    if (n % 5) == 0 and (n % 7) == 0:
        print('{} is divided by 5 and 7'.format(n))
    elif (n % 5) == 0:
        print('{} is divided by 5'.format(n))
    elif (n % 7) == 0:
        print('{} is divided by 7'.format(n))
    else:
        print('{} is not important'.format(n))

