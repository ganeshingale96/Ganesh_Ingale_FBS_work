# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not

def check(dic,key):
    #1.---------
    # for keys in dic.keys():
    #     if keys == key:
    #         return True
    #2.---------
    if key in dic.keys():
        return True

dic = {'Id':'FBS-50','Name':'Ganesh','Age':21}
key = input("Enter the key you wnt to check: ")
if check(dic,key):
    print(f'{key} Key Exists in a Dictionary')
else:
    print(f'{key} Key Not Exists in a Dictionary')