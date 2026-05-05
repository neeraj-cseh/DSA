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

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]
freq = [0] * 11
for i in n:
    freq[i] +=1
for i in m:
    if i < 0 or i > 10:
        print(i, "->", 0)
    else:
        print(i, "->", freq[i])