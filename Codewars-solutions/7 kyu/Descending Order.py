"""
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
"""
def descending_order(num):
    num = str(num)
    num = [i for i in num]
    bigger_num = ''
    for k in range(len(num)):
        for i in range(1, len(num)):
            if num[-i] < num[-i - 1]:
                continue
            else:
                a = num[-i]
                num[-i] = num[-i - 1]
                num[-i - 1] = a
    for i in num:
        bigger_num += i
    return int(bigger_num)
print(descending_order(123456789))
