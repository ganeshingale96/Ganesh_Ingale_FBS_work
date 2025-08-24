def power_of_num(num):
    if num == 0:
        return 0
    else:
        return 1 + power_of_num(num // 10)

def armstrong(num):
    power = power_of_num(num)
    if num ==0:
        return 0
    else:
        return (num%10)**power + armstrong(num//10)
def check_armstrong(num):
    if num == armstrong(num):
        return True
    else:
        return False   

num = int(input("Enter the number: "))
res = check_armstrong(num)
if res:
    print(f'{num} is an Armstrong number')
else:
    print(f'{num} is not an Armstrong number')










