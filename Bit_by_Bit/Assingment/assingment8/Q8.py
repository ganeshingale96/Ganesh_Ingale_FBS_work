def reverse_of_num(num):
    reverse = 0
    num = num
    temp = 0
    c = 1
    for i in range(1,4):
        d = num%10
        num//=10
        
        if(c==1):
            temp = d*100
        elif(c==2):
            temp = d*10
        else:
            temp = d  
        c+=1   
        reverse+=temp
    return reverse

num = int(input("Enter the number: "))
result=reverse_of_num(num)
print(f'The reverse number of {num} is: {result}')



    