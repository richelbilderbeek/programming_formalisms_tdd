'''
`are_numbers(x)`         
`are_strings(x)`         
`check_are_numbers(x)`   
`check_different(a, b)`  
`check_equal(a, b)`      
`check_is_number(x)`     
`check_is_probability(p)`  
`check_is_string(x)`       
`divide_safely(a, b)`    
`is_dividable_by_three(x)`    |Returns `True` if `x` is dividable by 3
`is_even(x)`                  |Returns `True` if `x` is even
`is_number(x)`                |Returns `True` if `x` is a number
`is_odd(x)`                   |Returns `True` if `x` is odd
`is_probability(p)`           
`is_string(x)`                |Returns `True` if `s` is a string
`is_zero(x)`                  |Returns `True` if `x` is zero

### Medium

Name                          |Purpose
------------------------------|----------------------------------------------
`are_primes(x)`      
`are_primes(x, m)`            
`calc_p_is_prime(x, m)`       
`can_use_prime_method(x, m)`  
`get_all_prime_methods()`     |Returns all prime finding methods
`get_digits(n)`               |Returns all the digits of number `n`
`get_proper_divisors(n)`      |Returns all proper divisors of number `n`
`is_palindrome(n)`         
`is_palindrome(s)`         
`is_perfect(x)`            
`is_prime(x)`                 |Returns `True` if `x` is prime
`is_prime(x, m)`     
`is_prime_td(x)`     
`is_prime_ss(x)`              
`is_prime_ss(x, p)`        
`is_prime_method(m)`       
`is_roman_number(s)` 
`sum_digits(x)`            
`to_roman_number(s)` 

### Hard

Name                          |Purpose
------------------------------|----------------------------------------------
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
