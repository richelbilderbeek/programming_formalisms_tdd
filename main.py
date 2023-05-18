'''
`check_is_string(x)`       

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

def are_numbers(x):
    """
    Determine if `x` is one or more numbers.
    Numbers can be integer or floating point
    
    Returns `True` if `x` is one or more numbers.
    """
    if not isinstance(x, list):
        return False
    if len(x) == 0:
        return False
    for e in x:
        if not is_number(e):
            return False
    return True

def are_strings(x):
    """
    Determine if `x` is one or more strings.
    
    Returns `True` if `x` is one or more strings.
    """
    if not isinstance(x, list):
        return False
    if len(x) == 0:
        return False
    for e in x:
        if not is_string(e):
            return False
    return True

def check_are_numbers(x):
    """
    Determine if `x` is one or more numbers.
    If `x` is not one or more numbers, a `RuntimeError` is raised.
    
    Returns nothing.
    """
    if not are_numbers(x):
        raise RuntimeError(
            "'x' must be numbers. ",
            "Actual value of 'x': ", x
        )


def check_different(a, b):
    """
    Determine if `a` and `b` are different.
    
    Raises `RuntimeError` when not.
    
    Returns nothing.
    """
    if a == b:
        raise RuntimeError(
            "'a' and 'b' must be different. ",
            "Value of 'a': ", a
        )

def check_equal(a, b):
    """
    Determine if `a` and `b` are equal.
    
    Raises `RuntimeError` when not.
    
    Returns nothing.
    """
    if not a == b:
        raise RuntimeError(
            "'a' and 'b' must be equal. ",
            "Value of 'a': ", a, ". ",
            "Value of 'b': ", b
        )

def check_is_number(x):
    """
    Determine if `x` is a number.
    If `x` is not a number, a `RuntimeError` is raised.
    
    Returns nothing.
    """
    if not is_number(x):
        raise RuntimeError(
            "'x' must be a number. ",
            "Actual value of 'x': ", x
        )

def check_is_probability(x):
    """
    Determine if `x` is a probability.
    If `x` is not a probability, a `RuntimeError` is raised.
    
    Returns nothing.
    """
    check_is_number(x)
    if not is_probability(x):
        raise RuntimeError(
            "'x' must be a probability. ",
            "Actual value of 'x': ", x
        )

def check_is_string(x):
    """
    Determine if `x` is a string.
    If `x` is not a string, a `RuntimeError` is raised.
    
    Returns nothing.
    """
    if not is_string(x):
        raise RuntimeError(
            "'x' must be a string. ",
            "Actual value of 'x': ", x
        )

def divide_safely(a, b):
    """
    Divide `a` by `b`.
    If `a` or `b` are not a floating point number, a `TypeError` is raised.
    If `b` is `0.0`, a `RuntimeError` is raised.
    
    Returns `a` divided by `b`
    """
    if b == 0.0:
        raise RuntimeError(
            "'b' must not be zero"
        )
    return a / b

def is_dividable_by_three(x):
    """
    Determine if `x` is dividable by three.
    If `x` is not an integer number, a `TypeError` is raised.
    
    Returns `True` if `x` is dividable by three
    """
    if not isinstance(x, int):
        raise TypeError(
            "'number' must be a number. Actual type of 'number': ", type(x) 
        )
    return x % 3 == 0

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

def is_odd(x):
    """
    Determine if `x` is odd.
    If `x` is not an integer number, a `TypeError` is raised.
    
    Returns `True` if `x` is odd
    """
    return not is_even(x)

def is_probability(x):
    """
    Determine if `x` is a probability,
    i.e. a value between 0.0 and 1.0, including both 0.0 and 1.0.
    If `x` is not a floating point number, a `TypeError` is raised.
    
    Returns `True` if `x` is a probability
    """
    if not isinstance(x, float):
        raise TypeError(
            "'number' must be a floating point number. ",
            "Actual type of 'number': ", type(x) 
        )
    return x >= 0.0 and x <= 1.0

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
            "'number' must be a number. ",
            "Actual type of 'number': ", type(x) 
        )
    return x == 0

def test_are_numbers():
    assert are_numbers.__doc__
    assert not are_numbers(":-/")
    assert are_numbers([1, 2])
    assert are_numbers([1.1])
    assert not are_numbers([ ])
    assert not are_numbers(["1.2"])

def test_are_strings():
    assert are_strings.__doc__
    assert are_strings(["A"])
    assert are_strings(["A", "B"])
    assert not are_strings("A")
    assert not are_strings(3.14)
    assert not are_strings(["A", 3.14])
    assert not are_strings([])

def test_check_are_numbers():
    assert check_are_numbers.__doc__
    assert are_numbers([3.14])
    assert are_numbers([3.14, 42])
    assert not are_numbers("A")
    assert not are_numbers(3.14)
    assert not are_numbers(["A", 3.14])
    assert not are_numbers([])

def test_check_different():
    assert check_different.__doc__
    check_different(1.2, 1.3)
    check_different(1.2, "A")
    
    has_thrown = False
    try:
        check_different(1.1, 1.1)
    except RuntimeError:
        has_thrown = True
    assert has_thrown

    has_thrown = False
    try:
        check_different("1.1", "1.1")
    except RuntimeError:
        has_thrown = True
    assert has_thrown

def test_check_equal():
    assert check_equal.__doc__
    check_equal(1.2, 1.2)
    check_equal("A", "A")
    
    has_thrown = False
    try:
        check_equal(1.1, 1.2)
    except RuntimeError:
        has_thrown = True
    assert has_thrown

    has_thrown = False
    try:
        check_equal(1.1, "1.1")
    except RuntimeError:
        has_thrown = True
    assert has_thrown

def test_check_is_number():
    assert check_is_number.__doc__
    check_is_number(1.2)
    
    has_thrown = False
    try:
        check_is_number( [1.1, 1.2] )
    except RuntimeError:
        has_thrown = True
    assert has_thrown

    has_thrown = False
    try:
        check_is_number("1.1")
    except RuntimeError:
        has_thrown = True
    assert has_thrown

def test_check_is_probability():
    assert check_is_probability.__doc__
    check_is_probability(0.2)
    
    has_thrown = False
    try:
        check_is_probability( [0.1, 0.2] )
    except RuntimeError:
        has_thrown = True
    assert has_thrown

    has_thrown = False
    try:
        check_is_probability("0.1")
    except RuntimeError:
        has_thrown = True
    assert has_thrown

def test_check_is_string():
    assert check_is_string.__doc__
    check_is_string("A")
    
    has_thrown = False
    try:
        check_is_string( ["A", "B"] )
    except RuntimeError:
        has_thrown = True
    assert has_thrown

    has_thrown = False
    try:
        check_is_string(3.14)
    except RuntimeError:
        has_thrown = True
    assert has_thrown

def test_divide_safely():
    assert divide_safely.__doc__
    assert divide_safely(1.2, 0.3) > 0.0
    
    has_thrown = False
    try:
        divide_safely(1.1, 0.0)
    except RuntimeError:
        has_thrown = True
    assert has_thrown


def test_is_dividable_by_three():
    assert is_dividable_by_three.__doc__
    assert not is_dividable_by_three(2)

    has_thrown = False
    try:
        is_dividable_by_three(3.14)
    except TypeError:
        has_thrown = True
    assert has_thrown

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

def test_is_odd():
    assert is_odd.__doc__
    assert not is_odd(2)

    has_thrown = False
    try:
        is_odd(3.14)
    except TypeError:
        has_thrown = True
    assert has_thrown

def test_is_probability():
    assert is_probability.__doc__
    assert is_probability(0.1)
    assert not is_probability(1.2)
    assert not is_probability(-1.2)
    
    has_thrown = False
    try:
        is_probability("I am a string")
    except TypeError:
        has_thrown = True
    assert has_thrown

def test_is_string():
    assert is_string("Hello")
    assert not is_string( { "Hello", "too much strings" } )
    assert is_string.__doc__
    

def test_is_zero():
    assert is_zero.__doc__
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

if __name__ == "__main__":
    print("Start of tests")
    test_are_numbers()
    test_are_strings()
    test_check_are_numbers()
    test_check_different()
    test_check_equal()
    test_check_is_number()
    test_check_is_probability()
    test_check_is_string()
    test_divide_safely()
    test_is_dividable_by_three()
    test_is_even()
    test_is_number()
    test_is_odd()
    test_is_probability()
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
