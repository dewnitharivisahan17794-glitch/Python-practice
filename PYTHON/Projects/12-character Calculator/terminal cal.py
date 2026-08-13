Numbers=[]
Operators=[]

Enter=input('Enter your calculation(left to right Answers):')

for i in Enter:
    if i.isdigit():
        Numbers.append(i)
    else:
        Operators.append(i)

print('Numbers:',Numbers)
print('Operators:',Operators)
result=int(Numbers[0])
for i in range(len(Operators)):
    op=Operators[i]
    Next_num=int(Numbers[i+1])

    if op=='*':
        result*=Next_num
        
    elif op=='/':
        result/=Next_num
        
    elif op=='+':
        result+=Next_num
       
    elif op=='-':
        result-=Next_num
        
print('The left-to-right answer is:',result)
print('The correct answer is:',eval(Enter))


