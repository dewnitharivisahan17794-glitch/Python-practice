lst=(1,2,3,4,5,9,7,5)

i = iter(lst)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

#or

while True:
    try:
        print(next(i))
    except StopIteration:
        break              


 #both methord are correct , but easies and fastest way is last one.

