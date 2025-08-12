
k=0
for i in range(1,6):
    for  j in range(1,6-i):
        print(' ',end = ' ')
    for j in range(1,2):
        print('*',end = ' ')

    for  j in range(3,i+i):
        print(' ',end = ' ')
    if(i!=1):
        for j in range(1,2):
            print('*',end = ' ') 
    print()
    
for i in range(1,6):
    for  j in range(1,i):
        print(' ',end = ' ')
    for j in range(1,2):
        print('*',end = ' ')

    for  j in range(1,8-k):
        print(' ',end = ' ')
    k+=2
    if(i!=5):
        for j in range(1,2):
            print('*',end = ' ')
    print()

