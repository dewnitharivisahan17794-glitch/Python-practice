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


#make new itaration

class myit:
    def __init__(self):
        self.x=2

    def __iter__(self):
        return self

    def __next__(self):
        val=self.x
        self.x+=2
        return val

myObj=myit()

itr=iter(myObj)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))