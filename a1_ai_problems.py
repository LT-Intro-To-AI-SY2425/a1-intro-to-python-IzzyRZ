# Complete your individualized AI problems here

from typing import List, TypeVar
"""1. Number Properties
Write a program that takes a number as input and prints whether the number is even or odd.
2. Sum of Integers
Write a program that calculates the sum of all integers from 1 to a given number n (where n is provided by the user).
3. Factorial Calculation
Write a program that calculates the factorial of a number n (where n is provided by the user). Recall that the factorial of n (denoted as n!) is the product of all positive integers less than or equal to n.
4. Reverse a String
Write a program that takes a string and prints it in reverse order.
5. Palindrome Checker
Write a program that checks if a given string is a palindrome. A palindrome is a string that reads the same forwards and backwards (e.g., "madam" or "racecar").
6. Multiplication Table
Write a program that prints a multiplication table for numbers 1 through 10. The output should show the result of multiplying each number by every number in the range.
7. Prime Number Checker
Write a program that checks if a given number is a prime number. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
8. List Sum
Write a program that takes a list of integers and prints the sum of the integers in the list.
9. Temperature Converter
Write a program that converts a temperature from Celsius to Fahrenheit. The formula for conversion is F = C * 9/5 + 32, where F is the temperature in Fahrenheit and C is the temperature in Celsius.
10. Count Vowels
Write a program that counts the number of vowels (a, e, i, o, u) in a given string.
11. Odd Numbers in a List
Write a program that takes a list of integers and prints out all the odd numbers from the list.
12. Character Frequency
Write a program that takes a string and counts the frequency of each character in the string, then prints out the results."""

def evenOdd(n: int) -> str:
    if(n%2==0):
        return "even"
    else:
        return "odd"
assert evenOdd(1) == "odd", "evenOdd 1 fail"
assert evenOdd(2) == "even", "evenOdd 2 fail"

def sumIntegers(n: int) -> int:
    output=0
    while(n>0):
        output += n
        n -= 1
    return output
assert sumIntegers(5) == 5+4+3+2+1, "sumIntegers 5 fail"

def factorial(n: int) -> int:
    x=1
    while(n>0):
       x=x*n
       n-=1
    return x 
assert factorial(4) == 24, "factorial 4 failed"
assert factorial(1) == 1, "factorial 1 failed"

def reverseString(string: str) -> str:
    stringBackward = ""
    for i in range(1,len(string)+1):
        stringBackward += string[len(string)-i]
    return stringBackward

assert reverseString("clam") == "malc", "reverseString fail"

def palindromeCheck(string: str) -> bool:
    stringBackward = reverseString(string)
    if string == stringBackward:
        return True
    else:
        return False
assert palindromeCheck("ufoTofu") == True, "palindromeCheck UFO Tofu fail"
assert palindromeCheck("Notapalindrome") == False, "palindromeCheck Notapalindrome fail"

def multiplicationTable():
    for i in range(1,11):
        for j in range(1,11):
            product = i*j
            print(product)

def primeCheck(n: int) -> bool:
        if(n % 2 == 0):
            return False
        for x in range(3,n,2):
          if(n % x == 0):
                return False
        return True
assert primeCheck(4) == False, "Prime 4 canceled"
assert primeCheck(5) == True, "primeCheck 5 fail"

def sumList(lst: List[int]) -> int:
    sumOutput = 0
    for x in range(0,len(lst)):
        sumOutput += lst[x]
    return sumOutput

assert sumList([1,2,-5]) == -2, "sumList 1, 2, -5 fail"

def convertToFarenheit(C: float) -> float:
    F = (C*9/5)+32
    return F

assert convertToFarenheit(0) == 32, "convertToFarenheit 0 fail"
assert convertToFarenheit(22) == 71.6, "converToFarenheit 22 fail"

def vowelCount(string: str) -> int:
    count = 0
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    for i in range(0,len(string)):
        for j in range(0,len(vowels)):
            if string[i] == vowels[j]:
                count += 1
    return count

assert vowelCount("vOwel") == 2, "vowelCount vOwel fail"

def printOdd(lst: List[int]):
    for x in range(0,len(lst)):
        if lst[x] % 2 != 0:
            print(lst[x])

printOdd([1,2,3,4,5])

def frequencyCount(string: str):
    charactersUsed = []
    for x in range(0, len(string)):
        if string[x] not in charactersUsed:
            freq = 0
            char = string[x]
            charactersUsed.append(char)
            for element in string:
                if element == char:
                    freq += 1
            freqString = str(freq)
            print(char + " appeared " + freqString + " times")

frequencyCount("apple")