"""
Problem: Student number
Source: CSES
Topic: Math / Checksum / String processing

Key Idea:
Validate format, then compute checksum using weighted sum
and compare with check digit.

Time: O(n)
"""

def check_number(number):
    if len(number) != 9:
        return False
    if not number.isdigit():
        return False
    if number[0] != '0':
        return False
    
    
    multiplier = [3,7,1,3,7,1,3,7]
    total = 0
    for digit, weight in zip(number[:-1], multiplier):
        total += int(digit) * weight
    return (10 - (total % 10)) % 10 == int(number[-1])

if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False