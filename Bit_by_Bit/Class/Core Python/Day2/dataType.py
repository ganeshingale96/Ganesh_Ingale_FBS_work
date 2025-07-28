## <<<<<<<<<<<<<<<<<<<<<<<<<<<<Data_Types>>>>>>>>>>>>>>>>>>>>>>>>>>>
#-----Numeric----------
#1)int
i = 5
print(type(i))
#2)Float
i = 5.1
print(type(i))
#3)Complex
i = 5+1j
print(type(i))

#-----Text----------
text1 = "hello"
text2 = '''
first line
------
-----
last line
'''
print(type(text1))
print(type(text2))

#-----Sequence----------
# 1) LIst
li = [1,2,3,4,5,6]
print(type(li))

# 2) Tuple
tu = (1,2,3,4,5)
print(type(tu))

# 3) Range
r = range(1,10)
print(type(r))

#-----Mapping----------
# 1) dict
my_dict = {'a':'python','b':'java'}
print(type(my_dict))

#-----Set Type----------
# 1) Set
my_set = {1,2,3,4,5}
print(type(my_set))

# 2) Frozenset
fs = frozenset({1,2,3,4,5})
print(type(fs))

#-----Boolean----------
val1 = True
val2 = False
print(type(val1))
print(type(val2))

#-----None Type----------
val = None
print(type(val))



#<<<<<<<<<<<<<<<<<<<<<<<Output>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# <class 'int'>
# <class 'float'>
# <class 'complex'>
# <class 'str'>
# <class 'str'>
# <class 'list'>
# <class 'tuple'>
# <class 'range'>
# <class 'dict'>
# <class 'set'>
# <class 'frozenset'>
# <class 'bool'>
# <class 'bool'>
# <class 'NoneType'>


