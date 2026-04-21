# n = 5873
# num = n
# while num > 0:
#     last_digit = num % 10
#     print(last_digit)
#     num = num // 10

# n = 5873
# num = n
# count = 0
# while num > 0:
#     last_digit = num % 10
#     count += 1
#     num = num // 10
# print(count)

# from math import *
# def count_digit(num):
#     return int(log10(num) + 1)
# print(count_digit(5438))


# n = 1234
# num = n
# result = 0
# while num > 0:
#     lg = num % 10
#     result = (result * 10) + lg
#     num //= 10
# if result == n:
#     print(True)
# else:
#     print(False)

# n = 153
# num = n
# power = len(str(n))
# result = 0
# while num > 0:
#     digit = num % 10
#     result = (result) + (digit ** power)
#     num //= 10
# if result == n:
#     print(True)
# else:
#     print(False)

# def factors(n):
#     num = n
#     result = []
#     for i in range(1, n//2):
#         if num % i == 0:
#             result.append(i)
#     result.append(num)
#     print(result)
# factors(36)

# from math import sqrt as sq
# n = 36
# num = n
# result = []
# for i in range(1, int(sq(num)+1)):
#     if num % i == 0:
#         result.append(i)
#         if num // i != i:
#             result.append(num//i)
# print(sorted(result))

