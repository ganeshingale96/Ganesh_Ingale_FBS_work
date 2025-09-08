def notes(d,amo):
    count = 0
    for i in d:
            count += amo // i
            amo%=i
            
    return count


d = [2000,500,200,100,50,20,10,5]
amo = int(input("Enter the amount: "))
print(f'Maximum number fo note nedded: {notes(d,amo)}')