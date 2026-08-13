#filter function

A = [1,2,3,4,5,6,7,8,9]

y = list(filter(lambda x: x % 2 == 0, A))
print("Even numbers in the list:", y)  # Output: [2, 4, 6, 8]

#map function

B = [1,2,3,4,5]

z = list(map(lambda x: x * 2, B))
print("Doubled values in the list:", z)  # Output: [2, 4, 6, 8, 10]

#reduce function

from functools import reduce

C = [1,2,3,4,5]
w = reduce(lambda x, y: x + y, C)
print("Sum of values in the list:", w)  # Output: 15

