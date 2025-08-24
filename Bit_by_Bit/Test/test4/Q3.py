# 3. WAP to print following patterns :
# **********************
#                     *
#                   * 
#                 *   
#               *     
#            *      
#         *     
#      *      
#   *      
# **********************
for i in range(1,13):
    for j in range(1,23):
        if (i==1 or i==12 or j%2!=0 or j-i):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
      