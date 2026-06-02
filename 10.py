num = [1, 2, 1, 3, 6, 9, 5, 7, 9, 2, 6, 9]
freq = {}
for i in range (0, len(num)):
    if num[i] in freq:
        freq[num[i]] += 1
    else:
        freq[num[i]] = 1
print(freq)