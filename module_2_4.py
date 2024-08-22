numbers_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes_ = []
not_primes_ = []
for numbers_ in numbers_:
    if numbers_ == 1:
        continue
    is_primes_ = True
    for i in range(2, numbers_):
        if numbers_ % i ==0:
            is_primes_ = False
            break
    if is_primes_:
        primes_.append(numbers_)
    else:
        not_primes_.append(numbers_)

print("Primes:", primes_)
print("Not Primes:", not_primes_)