# -*- coding: utf-8 -*-
"""
@author: Saumitra Kulkarni
"""

def int2digits(n, base = 10):
    """
    Compute the base-b digits of a positive integer n
    """
    # digits = list()
    if n >= 0:
        digits = list()
        while n:
            digits.append(n % base)
            n = n // base
        return digits

def digits2int(digits, base = 10):
    """
    Compute a positive integer n given an array d of its the base-b digits
    """
    n = 0
    if len(digits) == 0:
        return None
    else:
        for i in range(len(digits)):
            n = n + (digits[i] * base**(i))
        return n

def kaprekar_step(n, ndigits = 4, base = 10, pad = True):
    """
    Apply one Kaprekar step to integer n with at most k base-b digits
    """
    digits = sorted(int2digits(n, base = base))
    if pad:
        digits =  [0] * max( 0, ndigits - len(digits)) + digits
    return digits2int(digits, base = base) - digits2int(list(reversed(digits)), base = base)

def kaprekar_routine(n, ndigits = 4, base = 10, pad = True):
    """
    Apply the Kaprekar routine to integer n with at most k base-b digits
    """
    orbit = list()
    while not(n in orbit):
        orbit.append(n)
        n = kaprekar_step(n)
    orbit.append(n)
    #orbit = np.array(orbit)
    i = orbit.index(n)
    return {'orbit': orbit, 'transient_length': i, 'cycle_start': i,
            'cycle_end': len( orbit ), 'cycle_period': len( orbit ) - i }
