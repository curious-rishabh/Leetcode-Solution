# Remainder without using modulo %
number = 9
divisor = 4

remainder = number - divisor * (number//divisor)

# Method 2
def getRemainder(num, divisor):
    while divisor <= num:
        num -= divisor
    return num

print(getRemainder(2, 2))
print(remainder)