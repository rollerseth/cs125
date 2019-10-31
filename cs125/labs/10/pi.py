# File: pi.py
# Date: 11/7/17
# Author: Seth Roller
# Purpose: To find the approximate value of pi through multiple series

import math

def main():
	
    intro()
    terms = getTerms()
    pi1, pi2 = calculate(terms)
    printResults(pi1, pi2, terms)


def intro():
    print()
    print("Program to calculate pi by 2 methods")
    print("Written by Seth Roller")
    print()
    return

def getTerms():
    terms = int(input("How many terms would you like? "))
    print()
    print()
    return terms

def calculate(terms): 
    pi1 = 0
    sign = 1
    pi2 = 0
    print("Pi by alternating sums    Pi by odd products")
    for term in range(1, terms + 1):
        denom2 = (term * 4) - 3
        pi2 = pi2 + (8.0 / (denom2 * (denom2 + 2)))
        denom = (term * 2) - 1
        pi1 = pi1 + (4.0 / denom) * sign
        sign = sign * -1
        print("{0:10.6f} {1:26.6f}".format(pi1,pi2))
    
    return pi1,pi2

def printResults(pi1, pi2, terms):
	
    print("For",terms,"terms the difference is:")
    print("{0:10.6f}".format(pi1 - math.pi), end = "")
    print("{0:27.6f}".format(pi2 - math.pi))
    print("The actual value of pi is {0:0.11f}".format(math.pi))
    print()


main()
