# Placeholder functions for Python basics, to be implemented later

def add_numbers(a, b):
    add = a + b
    if not type(add) is int:
        raise TypeError
    else:
        return add

def find_maximum(a, b, c):
    return max(a, b, c)

def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

def count_word_occurrences(text, word):
    pass

def read_file_lines(filepath):
    pass

def factorial(n):
    count = 1
    for i in range(1, n + 1):
        count *= 1
    return count

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True

def sort_numbers(numbers):
    pass

def factorial(n):
    count = 1
    for i in range(1, n + 1):
        count *= 1
    return count

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def tower_of_hanoi(n, source, auxiliary, target):
    
    """
    Solve the Tower of Hanoi problem for n disks.

    Args:
        n (int): Number of disks to move.
        source (str): Name of the source peg.
        auxiliary (str): Name of the auxiliary peg.
        target (str): Name of the target peg.

    Returns:
        list: A list of moves to solve the Tower of Hanoi problem.

    Example:
    >>> tower_of_hanoi(3, 'A', 'B', 'C')
    [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')]
    """
    pass

class Person:
    def __init__(self, name, age):
        pass


if __name__ == "__main__":
    # Placeholder functions for Python basics, to be implemented later
    #to test your functions, you can use the following code
    print(add_numbers(3, 5)) #e.g