for i in range(1,5):
    for j in range(i,i+i):
        if i==3:
            print(j+1,end = ' ')

        elif i==4:
            print(j+3,end = ' ')
    
        else:
            print(j,end = ' ')
        
    print()