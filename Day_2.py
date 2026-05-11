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

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
# arr = [5,7, 8, 4, 1, 6, 9, 2]
# selection_sort(arr)
# print(arr)

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n-2, -1, -1):
#         for j in range(0, i+1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
# arr = [5, 1, 6, 8, 2, 4, 9]
# bubble_sort(arr)
# print(arr)

# arr = [3, 5, 6, 4, 8, 9, 10, 7, 1]
# n = len(arr)
# for i in range(1,n):
#     key = arr[i]
#     j = i - 1
#     while j >= 0 and arr[j] > key:
#         arr[j + 1] = arr[j]
#         j -= 1
#     arr[j + 1] = key
# print(arr)

# def insertion_sort(arr):
#     n = len(arr)
#     for i in range (1, n):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
# arr = [3, 5, 6, 4, 8, 9, 10, 7, 1]
# insertion_sort(arr)
# print(arr)

# def merge_arr(left, right):
#     result = []
#     i, j = 0, 0
#     n, m = len(left), len(right)
#     while i < n and j < m:
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     if i < n:
#         while i < n:
#             result.append(left[i])
#             i += 1
#     if j < m:
#         while j < m:
#             result.append(right[j])
#             j += 1
#     return result
    
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left_arr = arr[:mid]
#     right_arr = arr[mid:]
#     left = merge_sort(left_arr)
#     right = merge_sort(right_arr)
#     return merge_arr(left, right)
    
# arr = [3, 1, 2, 4, 1, 5, 2, 6, 4]
# print(merge_sort(arr))

