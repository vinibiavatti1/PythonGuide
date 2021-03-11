"""
Cache decorator
"""


def cache(func):
    def wrapper(number, **kwargs):
        if not kwargs.get('cache', True):
            return func(number)
        if hasattr(func, '_cache'):
            if kwargs.get('clear_cache', False):
                func._cache = {}
            if number in func._cache:
                print('[From cache]', end=' ')
                return func._cache[number]
        else:
            func._cache = {}
        result = func(number)
        func._cache[number] = result
        return result
    return wrapper


@cache
def get_prime_numbers_until(number, **kwargs):
    primes = []
    for n in range(2, number + 1):
        divisible = False
        for i in range(2, n):
            if n % i == 0:
                divisible = True
                break
        if not divisible:
            primes.append(n)
    return primes


print(get_prime_numbers_until(5))   # [2, 3, 5]
print(get_prime_numbers_until(10))  # [2, 3, 5, 7]
print(get_prime_numbers_until(5))   # [From cache] [2, 3, 5]
print(get_prime_numbers_until(10))  # [From cache] [2, 3, 5, 7]

print(get_prime_numbers_until(5, clear_cache=True))
# [2, 3, 5]

print(get_prime_numbers_until(10))  # [2, 3, 5, 7]
print(get_prime_numbers_until(5))   # [From cache] [2, 3, 5]

print(get_prime_numbers_until(5, cache=False))
# [2, 3, 5]
