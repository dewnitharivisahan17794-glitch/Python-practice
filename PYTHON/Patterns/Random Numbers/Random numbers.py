import random

X=random.random() #between  (0-1)
print(X)

Y=random.random()*10 #between  (0-10)
print(Y)

Z=random.randint(1,100) #between  (1-100)#raindint() returns a random integer between the two specified numbers.
print(Z)

K=random.uniform(5,100) #between  (5-100)
print(K)

Name=["John","Mike","Sam","Tom","Harry","Ron","Hermione","Draco"] #list of names
winner=random.choice(Name) #randomly selects a name from the list
print(f"The winner is {winner}")

Name.remove(winner) #removes the winner from the list

winner_for_1lkh=random.shuffle(Name) #randomly shuffles the list of names
print(f"first 2 are choosen to 100,000 prizes {Name[0]} and {Name[1]}")