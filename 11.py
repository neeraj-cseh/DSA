n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]
freq = [0] * 11
for i in n:
    freq[i] += 1
for i in m:
    if i < 0 or i > 10:
        print(i, "-> 0")
    else:
        print(i, "->", freq[i])