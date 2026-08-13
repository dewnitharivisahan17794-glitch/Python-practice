with open('PYTHON/File handling/Hello.txt', 'r') as x:#(r is read mode)
    print(x.read())


with open('PYTHON/File handling/Hello.txt', 'r') as x:
    print(x.readline())
    print(x.readline())
    print(x.readline())

    print(x.readlines())

with open('PYTHON/File handling/Hello.txt', 'w') as x:#(in this mode, all contents are deleted and re written)
    x.write("Hello, World!")
    x.write("\nThis is a new line.")
    x.write("\nThis is another new line.")

    