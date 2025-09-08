def freq(n):
    dict ={}
    for i in range(1,n):
        coin = int(input())
        if coin in dict:
            dict[coin]+=1
        else:
            dict[coin]=+1
    for i,j in dict.items():
        if j%2!=0:
            return i

n = int(input("Enter the number:"))
print(f'Missing coin: {freq(n)}')