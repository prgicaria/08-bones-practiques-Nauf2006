#!/usr/bin/env python
dividend = int(input("Enter the dividend:"))
divisor = int(input("Enter the divisor:"))

quotient = dividend // divisor
Residu = dividend % divisor

print(f"Divisió: {dividend}/{divisor}")
print(f"Quotient: {quotient}")
print(f"Remainder: {Residu}")
