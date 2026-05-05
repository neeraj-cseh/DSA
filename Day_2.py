# arr = [1, 2, 1, 1, 2, 3, 4]
# count = {}
# for i in arr:
#     count[i] = count.get(i, 0) + 1
# print(count)

# n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
# m = [10, 111, 1, 9, 5, 67, 2]
# frequency = {}
# for i in n:
#     frequency[i] = frequency.get(i, 0) + 1
# for j in m:
#     print(j, "->", frequency.get(j, 0)) 

# n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
# m = [10, 111, 1, 9, 5, 67, 2]
# hash = [0] * 11
# for i in n:
#     hash[i] += 1
# for i in m:
#     if i < 0 or i > 10:
#         print(i, "->", 0)
#     else:
#         print(i, "->", hash[i])

# def greet():
#     print("Hello")
#     greet()
# greet()

# arr = [34, 7, 23, 32, 5, 62]
# first = second = float('inf')
# for i in arr:
#     if i < first:
#         second = first
#         first = i
#     elif i < second and i != first:
#         second = i
# print(second)

# n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
# m = [10, 111, 1, 9, 5, 67, 2]
# freq = [0] * 11
# for i in n:
#     freq[i] +=1
# for i in m:
#     if i < 0 or i > 10:
#         print(i, "->", 0)
#     else:
#         print(i, "->", freq[i])

# count = 0
# def fun():
#     global count
#     if count == 5:
#         return
#     print("Hello")
#     count += 1
#     fun()
# fun()

# count = 0
# def fun():
#     global count 
#     if count == 5:
#         return
#     count += 1
#     fun()
#     print("Hello")
# fun()

# def fun(x, n):
#     if n == 0:
#         return
#     print(x)
#     fun(x, n-1)
# fun("Hello", 5)

# def fun (x, n):
#     if x > n:
#         return
#     print(x)
#     fun(x+1, n)
# fun(1, 5)

# def fun (x, n):
#     if x > n:
#         return
#     fun(x+1, n)
#     print(x)
# fun(1, 5)

# def fun(n):
#     if n == 0:
#         return
#     print(n)
#     fun(n - 1)
# fun(5)

# def fun(n):
#     if n == 0:
#         return
#     fun(n - 1)
#     print(n)
# fun(5)

# def fun(sum, x, n):
#     if x > n:
#         print(sum)
#         return
#     fun(sum+x, x+1, n)
# fun(0, 1, 5)

# def fun(n):
#     if n == 0:
#         return 0
#     return n + fun(n - 1)
# print(fun(5))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))

# arr = [5, 7, 3, 2, 6, 1, 5, 9]
# def reverse(arr, left, right):
#     if left >= right:
#         return
#     arr[left], arr[right] = arr[right], arr[left]
#     reverse(arr, left + 1, right - 1)
# reverse(arr, 0, len(arr) - 1)
# print(arr)

# s = 'abcdcba'
# left = 0
# right = len(s) - 1
# while left < right:
#     if s[left] != s[right]:
#         print(False)
#         break
#     left += 1
#     right -= 1
# else:
#     print(True)

# def pal(s, left, right):
#     if left >= right:
#         return True
#     if s[left] != s[right]:
#         return False
#     return pal(s, left + 1, right - 1)
# s = 'abcdcba'
# print(pal(s, 0, len(s) - 1))

# def fib(n):
#     if n == 1 or n == 0:
#         return n
#     return fib(n - 1) + fib(n - 2)
# print(fib(6))

