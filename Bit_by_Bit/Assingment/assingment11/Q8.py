# 8. Print 1 to 100 in snakes and ladder pattern.
num = 1
board = []
for j in range(100,0,-10):
    row = []
    if num%2!=0:
        for i in range(j,j-10,-1): 
            row.append(i)
    else:
        for k in range(j-9,j+1,+1):
            
            row.append(k)
    num+=1
    board.append(row)
print(board)






