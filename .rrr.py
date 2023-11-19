# def answer1():
#     num1 = float(input('請輸入數字1 :'))
#     num2 = float(input('請輸入數字2 :'))

#     print(f'總和 : {num1 + num2}')
#     print(f'總和 : {(num1 + num2)/2}')
# answer1()

# def answer2(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#     return total
# print(answer2(3))

# def answer3(word):
#     if type(word) != str:
#         print('[*] word must be str')
#     else:
#         a = ''
#         for w in word:
#             a = w + a
#         return a
# result = answer3("abcde")
# print(result)


# 費氏數列
# 解法以下幾種:
# for loop
# recursive
# dynamic programming (dp)

def fibonacci(n):
    if n == 1 or n==2:
        return 1
    r = 0
    a1 = 1
    a2 = 1
    for i in range(1, n-1):
        r = a1 + a2
        a1 = a2
        a2 = r
    return r
print(fibonacci(3))


for i in range(1,32):
    print(f'第{i}項費氏數列質為:{fibonacci(i)}')








