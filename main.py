'''
`are_numbers(x)`              |Returns `True` if `x` is zero, one or more numbers
`are_strings(x)`              |Returns `True` if `x` is zero, one or more strings
`check_are_numbers(x)`        |Throws a helpful error if `x` is not zero, one or more numbers
`check_different(a, b)`       |Throws a helpful error if `a` and `b` are not different
`check_equal(a, b)`           |Throws a helpful error if `a` and `b` are different
`check_is_number(x)`          |Throws a helpful error if `x` is not a number
`check_is_probability(p)`  
`check_is_string(x)`       
`divide_safely(a, b)`         |Divide `a` by `b`, throws a helpful error if `b` is zero
`is_dividable_by_three(x)`    |Returns `True` if `x` is dividable by 3
`is_even(x)`                  |Returns `True` if `x` is even
`is_number(x)`                |Returns `True` if `x` is a number
`is_odd(x)`                   |Returns `True` if `x` is odd
`is_probability(p)`           
`is_string(x)`                |Returns `True` if `s` is a string
`is_zero(x)`                  |Returns `True` if `x` is zero

### Medium

Name                          |Purpose
------------------------------|-----------------------------------------------------------------------
`are_primes(x)`               |Returns `True`/`False` for each element in `x` being prime yes/no
`are_primes(x, m)`            
`calc_p_is_prime(x, m)`       
`can_use_prime_method(x, m)`  
`get_all_prime_methods()`     |Returns all prime finding methods
`get_digits(n)`               |Returns all the digits of number `n`
`get_proper_divisors(n)`      |Returns all proper divisors of number `n`
`is_palindrome(n)`            |Returns `True` if the number `n` is a palindrome
`is_palindrome(s)`            |Returns `True` if the string `s` is a palindrome
`is_perfect(x)`               |Returns `True` if `x` is a perfect number
`is_prime(x)`                 |Returns `True` if `x` is prime
`is_prime(x, m)`              |Returns `True` if `x` is prime using method `m`
`is_prime_td(x)`              |Returns `True` if `x` is prime using the Trial Division method
`is_prime_ss(x)`              
`is_prime_ss(x, p)`        
`is_prime_method(m)`          |Returns `True` if `m` is a prime finding method
`is_roman_number(s)`          |Returns `True` if `s` is a string that is a roman number
`sum_digits(x)`               |Returns the sum of the digits of number `x`
`to_roman_number(s)`          |Returns a number equivalent to the roman number that is string `s`

### Hard

Name                          |Purpose
------------------------------|-----------------------------------------------------------------------
`calc_p_is_prime_bpsw(x)`     
`calc_p_is_prime_mr(x)`       
`calc_p_is_prime_ss(x)`       
`is_coprime(a, b)`            |Returns `True` is `a` is coprime to `b`
`is_factorial_prime(x)`       |Returns `True` if `x` is a factorial prime
`is_mersenne_prime(x)`        |Returns `True` if `x` is a Mersenne prime
`is_proth_prime(x)`           |Returns `True` if `x` is a Proth prime
`is_perfect_power(x)`         |Returns `True` if `x` is a perfect power
`is_prime_aks(x)`             
`is_prime_bpsw(x)`            
`is_prime_ec(x)`              
`is_prime_ec(x, m)`           
`is_prime_eccm(x)`            
`is_prime_ecpp(x)`            
`is_prime_ecgk(x)`            
`is_prime_mr(x)`              
`is_primorial_prime(x)`       |Returns `True` if `x` is a primorial prime
`is_twin_prime(x)`            |Returns `True` if `x` is a twin prime
'''

def is_zero(x):
    if not isinstance(x, int):
        raise TypeError(
            "'number' must be a number"
        )
    return x == 0


if __name__ == "__main__":
    print("Start of tests")
    
    if "is_zero":
        assert is_zero(0)
        assert not is_zero(1)
        assert not is_zero(1)

        has_thrown = False
        try:
            is_zero("")
        except TypeError:
            has_thrown = True
        assert has_thrown
    
    
    print("All tests passed")
