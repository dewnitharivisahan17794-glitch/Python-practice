# User defined function are the functions which are defined by the user to perform a specific task. 
# The user can define a function using the def keyword followed by the function name and parentheses. 
# The function can take parameters and can return a value.

def midpo(num1,num2):
    mid=(num1 + num2)/2
    print("The mid point is",mid)

midpo(12,71)
midpo(23,45)

def area_of_circle(radius):
    area=3.14*radius*radius
    print("The area of the circle is",area)

area_of_circle(5)
area_of_circle(7.5)

#Arguments

def student(subject="python", marks="ab"):
    print("subject is = ",subject)
    print("marks is =",marks)

student()
student("Mathematics")
student("Physics", "excellent")

def Group(Group_Name,Leader_Name,*members):
    print("Group Name:", Group_Name)
    print("Leader Name:", Leader_Name)
    print("Members:", members)

Group("Alpha", "John", "Alice", "Bob", "Charlie")

def Group(Group_Name,Leader_Name,**members):
    print("Group Name:", Group_Name)
    print("Leader Name:", Leader_Name)
    print("Members:", members)

Group("Beta", "Jane", Alice="Treasurer", Bob="Co-Leader", Charlie="Member", David="Member", Magret="Member")

def Group(Group_Name,Leader_Name,**members):
    print("Group Name:", Group_Name)
    print("Leader Name:", Leader_Name)
    print("Members:", members)

    for member, role in members.items():
        print(f"(Name: {member}, role: {role})")

Group("Beta", "Jane", Alice="Treasurer", Bob="Co-Leader", Charlie="Member", David="Member", Magret="Member")

