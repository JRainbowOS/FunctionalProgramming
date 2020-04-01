from typing import List

from decorators import timer

def qsort(a: List):
    if a == []:
        return a
    else:
        pivot, xs = a[0], a[1:]
        a_lesser = [num for num in xs if num < pivot]
        a_greater = [num for num in xs if num >= pivot]
        return qsort(a_lesser) + [pivot] + qsort(a_greater)
 
@timer
def quicksort(a: List):
    return qsort(a)      

def main():
    a = [1, 3, 2, 4, 0]
    print(quicksort(a))

if __name__ == '__main__':
    main()