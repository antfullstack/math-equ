def power(base, exponent):
    return base ** exponent

#Takes a number and until it is equal to 0 it multiplies it with its previous in order storing the new result.
def factorial(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1    
    return result

#Implementation based on the Eucledean algorithm.
def gcd(a, b):
    if b == 0: 
        return a
    return gcd(b, a % b)

