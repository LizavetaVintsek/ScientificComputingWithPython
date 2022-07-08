# Reversing a part of a list in place, reverse_range(L, left, right),
# the right index is included. Write iterative and recursive versions.
#var1
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
strt, end = 3, 7
L[strt:end] = L[strt:end][::-1]
print(L)
#var2
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L.insert(3,L.pop(6))
L.insert(4,L.pop(6))
L.insert(5,L.pop(6))
print (L)
#var3
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3
L[n], L[n+1], L[n+2], L[n+3] = L[n+3], L[n+2], L[n+1], L[n]
print(L)

#iteration1
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
strt, end = 3, 7
LRev = L[strt:end]
LRev.reverse()
for idx in range(strt, end):
    L[idx] = LRev[idx - strt]
print(L)
#iteration2
def reverse_range1(L, right, left):
    while left < right:
        x = L[left]
        L[left] = L[right]
        L[right] = x
        left = left+1
        right = right-1
    L = list(range(10))
reverse_range1(L, 2, 7)
print(L)

#recursive
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def reverse_range2 (L, left, right):
    if left < right:
        L[left], L[right] = L [right], L [left]
        reverse_range2(L, left+1, right-1)
reverse_range2 (L, 3, 6)
print(L)
