def is_prime(num):
    count = 0
    if num > 0:
        for i in range(1, num + 1):
            if num % i == 0:
                count = count + 1
        if count > 2:
            return False
        else:
            return True


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
