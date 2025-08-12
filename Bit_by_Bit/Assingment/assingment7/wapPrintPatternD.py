k = 2
t = 1
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')
    for j in range(i,i+i):
        print(j,end=' ')
    if(i!=1):
        for j in range(k,t,-1):
        
            print(j,end=' ')
        k+=2
        t+=1
    
    
    print()