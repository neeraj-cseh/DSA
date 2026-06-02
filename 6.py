num = 12345
n = num
count = 0
while n > 0:
    last = n % 10
    count += 1
    n = n //10
print(count)