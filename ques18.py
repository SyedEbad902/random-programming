import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

a, b = 12, 18
lcm_result = lcm(a, b)
lcm_result
