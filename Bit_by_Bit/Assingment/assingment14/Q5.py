# 5. Write a Python program to find the longest common prefix of all
# strings. Use the Python set.
li = ['gane','ganes','ganesh','gan']
perfix = list()
res=""
min_len = len(li[0])
for i in range(len(li)):
    if min_len > len(li[i]):
        min_len = len(li[i])

for i in range(min_len):
    for j in range(1,len(li)):
        if li[0][i] == li[j][i]:
            continue
        else:
            break

    else:
        res = res+li[0][i]
print("the longest common prefix of all strings is:",res)

