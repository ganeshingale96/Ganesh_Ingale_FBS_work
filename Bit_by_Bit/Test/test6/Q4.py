def freq(li):
    dict ={}
    for ele in li:
        if ele in dict:
            dict[ele]+=1
        else:
            dict[ele]=1
    return dict

li = [1,2,3,4,5,6,7,8,1,2,4,6]
print(f'frequency of occurence: {freq(li)}')
    