# 2. Python Program to Concatenate Two Dictionaries Into One

def Concat(dic,dic1):
    dic.update(dic1)
    return dic
dic = {'Name':'Ganesh'}
dic1 = {'ID':'FBS-50'}
print(f'After the Concatenate Two Dictionaries Into One: {Concat(dic,dic1)}')
