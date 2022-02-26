_primes = {2, 3, 5}


def get_primes(size: int):
    global _primes
    i_ = max(_primes) + 2
    while True:
        c = False
        for prime in _primes:
            if i_ % prime == 0:
                c = True
                break
            c = False
        if not c:
            _primes.add(i_)
        if len(_primes) >= size:
            break
        i_ += 2
    return _primes
