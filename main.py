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
`(x)`                  |Returns `True` if `x` is even
`is_odd(x)`                   |Returns `True` if `x` is odd
`is_probability(p)`           

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

def is_even(x):
    """
    Determine if `x` is even.
    If `x` is not an integer number, a `TypeError` is raised.
    
    Returns `True` if `x` is even
    """
    if not isinstance(x, int):
        raise TypeError(
            "'number' must be a number. Actual type of 'number': ", type(x) 
        )
    return x % 2 == 0

def is_number(x):
    """
    Determine if `x` is one number,
    for example, '42' or '3.14.
    
    Returns `True` if `x` is one number
    """
    return isinstance(x, (int, float) )

def is_string(x):
    """
    Determine if `x` is one string
    
    Returns `True` if `x` one string
    """
    return isinstance(x, str)

def is_zero(x):
    """
    Determine if `x` is zero.
    If `x` is not a number, a `TypeError` is raised.
    
    Returns `True` if `x` is zero
    """
    if not isinstance(x, (int, float)):
        raise TypeError(
            "'number' must be a number. Actual type of 'number': ", type(x) 
        )
    return x == 0

def test_is_even():
    assert is_even.__doc__
    assert not is_even(1)

    has_thrown = False
    try:
        is_even(3.14)
    except TypeError:
        has_thrown = True
    assert has_thrown


def test_is_number():
    assert is_number.__doc__
    assert is_number(42)
    assert is_number(3.14)
    assert not is_number("a string")

def test_is_string():
    assert is_string("Hello")
    assert not is_string( { "Hello", "too much strings" } )
    assert is_string.__doc__
    

def test_is_zero():
    assert is_zero(0)
    assert is_zero(0.0)
    assert not is_zero(1)
    
    has_thrown = False
    try:
        is_zero( { 1, 2 } )
    except TypeError:
        has_thrown = True
    assert has_thrown

    has_thrown = False
    try:
        is_zero("I am a string")
    except TypeError:
        has_thrown = True
    assert has_thrown

    assert is_zero.__doc__

if __name__ == "__main__":
    print("Start of tests")
    test_is_even()
    test_is_number()
    test_is_string()    
    test_is_zero()
    
    # Show the documentation
    print(is_zero.__doc__)

    # Show an exception
    try:
        is_zero("should be a number")
    except TypeError as e:
        print(e)
    
    
    print("All tests passed")
