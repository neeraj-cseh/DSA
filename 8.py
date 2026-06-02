num = int(input("Enter a number: "))
n = num
power = len(str(num))
total = 0
while n > 0:
    digit = n % 10
    total = total + digit ** power
    n = n // 10
if total == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")