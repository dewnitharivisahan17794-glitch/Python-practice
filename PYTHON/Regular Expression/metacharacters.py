import re
#metacharacters used in regular expressions
# . ^ $ * + ? { } [ ] \ | ( )

Hello = "Hello, welcome to the world of Python"
Game="my age is 20 and do you like to work with me?"
# . (dot) matches any character except a newline
y=re.findall(".",Hello)
print(y)
# ^ (caret) matches the start of the string
y=re.findall("^Hello",Hello)
print(y)    
# $ (dollar) matches the end of the string
y=re.findall("Python$",Hello)   
print(y)
# * (star) matches zero or more occurrences of the preceding character
y=re.findall("o*",Hello)        
print(y)
# + (plus) matches one or more occurrences of the preceding character
y=re.findall("o+",Hello)    
print(y)
# ? (question mark) matches zero or one occurrence of the preceding character
y=re.findall("o?",Hello)    
print(y)

y=re.findall("o{2}",Hello)
print(y)
#/w= matches any alphanumeric character (letters and digits) and underscore
y=re.findall("\w{2,5}",Hello)
print(y)
y=re.findall("\w{2}",Game)
print(y)
y=re.findall("\w\w\W",Game)
print(y)
#/d= matches any digit (0-9)
y=re.findall("\d{1,3}",Game)
print(y)
