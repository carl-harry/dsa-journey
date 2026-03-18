def ceil_div(a, b):
    """
    Performs ceiling division using only integer arithmetic.
    
    Useful for:
    - packing / grouping
    - pagination
    - binary search feasibility checks

    assumes b > 0. 
    """

    return (a + b - 1) // b