# 7. Python Program to Remove the Given Key from a Dictionary

def remove(dic,key):
    new_dic = {}
    if key not in dic.keys():
        return f'The enterd key is not present in dictionary'
    else:
        for keys , values in dic.items():
            if key!=keys:
                new_dic[keys]=values
    return new_dic

dic = {'Id':'FBS-50','Name':'Ganesh','Age':21}
key = input("Enter the key you want to remove from dictionry: ")
print(remove(dic,key))