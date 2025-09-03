# 2. Python Program to Merge Two Lists and Sort it
def merge_sort_list(li1,li2):
    new_list = li1+li2
    #1----------------------------------------------------------
    # for i in range(1,len(new_list)):
    #     for j in range(len(new_list)-1):
    #         if new_list[i]<new_list[j]:
    #             new_list[i],new_list[j]=new_list[j],new_list[i]
    #         print(new_list)
    # return  new_list
    #2----------------------------------------------------------
    # for i in range(1,len(new_list)):
    #     for j in range(len(new_list)-i):
    #         if new_list[j]>new_list[j+1]:
    #             new_list[j],new_list[j+1]=new_list[j+1],new_list[j]
    #         print(new_list)
    # return  new_list
    #3---------------------------------------------------------
   
    for i in range(len(new_list)-1):
        ind = i
        for j in range(i+1,len(new_list)):
            if new_list[ind]>new_list[j]:
                ind = j
        new_list[i],new_list[ind] = new_list[ind],new_list[i]
    return new_list

li1 = [1,2,34,21,23]      
li2 = [41,24,20,8]      
res = merge_sort_list(li1,li2)
print("List after sort:",res)


