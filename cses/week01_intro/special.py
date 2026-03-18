"""
Problem: Year 2025
Source: CSES
Topic: Math / Number manipulation

Key Idea:
Split year into halves and test condition.

Time: O(1)
"""

def check_year(year):
    first = year // 100 
    second = year % 100
    return (first + second) ** 2 == year

if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False