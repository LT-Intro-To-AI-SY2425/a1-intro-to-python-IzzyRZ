"""Assignment 1

Fill in the following function skeletons - descriptions are provided in 
the docstring (the triple quote thing at the top of each function)

Some assert statements have been provided - write more of them to test your code!

The `raise NotImplementedError(...)`s are placeholders to help you not skip implementing
a function. They should be removed and replaced with your solution.

This portion of the assignment will not be graded, but this gives you some problems to 
check, if you do not complete the generative AI portion of the assignment.
"""

from typing import List, TypeVar


def absolute(n: int) -> int:
    if(n<0):
        return -1*n
    else:
        return n
assert absolute(3) == 3, "absolute 3 failed"
assert absolute(0) == 0, "absolute 0 failed"
def factorial(n: int) -> int:
    x=1
    while(n>0):
       x=x*n
       n=n-1
    return x 
assert factorial(4) == 24, "factorial 4 failed"
assert factorial(1) == 1, "factorial 1 failed"

T=TypeVar('T')

def every_other(lst: List[T]) -> List[T]:
    outputList = []
    i=0
    while(i<len(lst)):
        outputList.append(lst(i))
        i+=2
    return outputList

def sum_list(lst: List[int]) -> int:
    sumOutput = 0
    for x in range(0,len(lst)):
        sumOutput += lst(x)
    return sumOutput


def mean(lst: List[int]) -> float:
    meanOutput = 0
    for x in range(0,len(lst)):
        meanOutput += len(x)
    meanOutput = meanOutput // len(x)
    return meanOutput


def median(lst: List[int]) -> float:
    
    raise NotImplementedError("median")


def duck_duck_goose(lst: List[str]) -> List[str]:
    """Given an list of names (strings), play 'duck duck goose' with it, knocking out
    every third name (wrapping around) until only two names are left.

    In other words, when you hit the end of the list, wrap around and keep counting from
    where you were.

    For example, if given this list ['Nathan', 'Sasha', 'Sara', 'Jennie'], you'd first
    knock out Sara. Then first 'duck' on Jennie, wrap around to 'duck' on Nathan and
    'goose' on Sasha - knocking him out and leaving only Nathan and Jennie.

    You may assume the list has 3+ names to start

    Args:
        lst - a list of names (strings)

    Returns:
        the resulting list after playing duck duck goose
    """
    raise NotImplementedError("duck_duck_goose")


# this line causes the nested code to be skipped if the file is imported instead of run
if __name__ == "__main__":
    assert absolute(-1) == 1, "absolute of -1 failed"
    assert factorial(4) == 24, "factorial of 4 failed"
    assert every_other([1, 2, 3, 4, 5]) == [
        1,
        3,
        5,
    ], "every_other of [1,2,3,4,5] failed"
    assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"
    assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"
    assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"

    names = ["roscoe", "kim", "woz", "solin", "law", "remess"]
    assert duck_duck_goose(names) == ["roscoe", "law"]

    print("All tests passed!")