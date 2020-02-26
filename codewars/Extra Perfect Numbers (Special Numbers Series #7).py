from math import sqrt


def extra_perfect(n):
    def isPrimes(n):
        if n > 1:
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for x in range(3, int(sqrt(n) + 1), 2):
                if n % x == 0:
                    return False
            return True
        return False

    return [x for x in range(3, n + 2, 2) if isPrimes(x)]


print(extra_perfect(7))