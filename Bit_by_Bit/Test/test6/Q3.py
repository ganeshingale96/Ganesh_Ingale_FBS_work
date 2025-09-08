def sort(data):
    for i in range(len(data)):
        for j in range(i,len(data)):
            if data[i][2]>data[j][2]:
                data[i],data[j]=data[j],data[i]
    return data

data = [[101,"seema",45000],[340,"Rajani",13000],[210,"Tannu",14000],[320,"Suresh",35000]]
print(f'After the sort list based on salary: {sort(data)}')