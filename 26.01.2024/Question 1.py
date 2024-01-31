'''
Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is better. For example, Kristen thinks that  is better than  and that  is better than .

Given an integer, , can you find the divisor of  that Kristin will consider to be the best?

Input Format

A single integer denoting .

Constraints

Output Format

Print an integer denoting the best divisor of .
#!/bin/python3

import math
import os
import random
import re
import sys
'''



def divisor(n):
    div = [i for i in range(1,n+1) if n%i==0]
    return max(div,key=lambda x: sum(int(i) for i in str(x)))

if __name__ == '__main__':
    n = int(input().strip())
    print(divisor(n))
