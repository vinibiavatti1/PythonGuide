"""
Cache decorator

* Create a cache decorator that will store the result of the function for the
  args
"""
from functools import wraps
from time import time


###############################################################################
# Decorator
###############################################################################


# Cache decorator
def cache(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # disable cache
        if not kwargs.get('cache', True):
            return func(*args, **kwargs)
        if kwargs.get('cache', False):
            del kwargs['cache']

        # generate cache key
        cache_key = ''
        sep = ''
        for arg in args:
            cache_key += sep + str(arg)
            sep = '__'
        for arg in kwargs.values():
            cache_key += sep + str(arg)
            sep = '__'

        # check cache
        if not hasattr(wrapper, 'cache'):
            wrapper.cache = {}
        if wrapper.cache.get(cache_key):
            return wrapper.cache.get(cache_key)

        # execute and store
        result = func(*args, **kwargs)
        wrapper.cache[cache_key] = result
        return result
    return wrapper


###############################################################################
# Decorated functions
###############################################################################


# Fibonatti function
@cache
def fib(amount, **kwargs):
    x, y = 1, 1
    result = []
    for _ in range(amount):
        result.append(x)
        x, y = y, x + y
    return result


# Sum range function
@cache
def sum_range(start, end, initial=0, **kwargs):
    result = initial
    for i in range(start, end):
        result += i
    return result


###############################################################################
# Algorithm
###############################################################################


# Main
def main(cache):
    start = time()
    fib(1000, cache=cache)
    sum_range(10, 100_000_000, cache=cache)
    print(f'Execution time: {time() - start} seconds')


# Init
if __name__ == '__main__':
    main(True)   # cache true
    main(True)   # cache true
    main(False)  # cache false
    # Execution time: 4.411196708679199 seconds (not in cache)
    # Execution time: 0.0 seconds               (got from cache)
    # Execution time: 4.546623229980469 seconds (ignored cache)
