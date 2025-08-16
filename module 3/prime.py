print('-------------')


# functie care returneaza primele 100 de numere primi

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


prime = []
n = 2
while len(prime) < 100:
    if is_prime(n):
        prime.append(n)
    n = n + 1

print(prime)






print("-----varianta Robert din timpul sedintei----")
def prime():
    prime_counter = 0
    nrs = 3
    result_in_function=["1", "2"]
    while prime_counter <= 100:
        for i in range(2, nrs // 2 + 1):
            if not nrs % i:
                break
        else:
            prime_counter = prime_counter + 1
            result_in_function.append(nrs)
        nrs = nrs + 1

    return result_in_function
print(__name__)
if __name__ == '__main__': #cand importam

    result = prime()
    print(result)
    print("------------------------")

