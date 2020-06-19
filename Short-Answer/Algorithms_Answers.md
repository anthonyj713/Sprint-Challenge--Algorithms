#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Only doing one function per loop. The higher n is, the longer it'll take but it grows linearly with n.

Answer: O(n)

b) With the nested loop, the time complexity should be O(n^2)

Answer: O(n^2)

c) With the recursion and adding 2 with the bunnyEars while the count of bunnies goes down 1 at a time, the time complexity should be O(2n)

Answer: O(2n)

## Exercise II

To minimize the amount of eggs that break, we need to assume that the building goes to a max story and not to infinity. With having a bottom floor = min and top floor = max, we can do a binary search to remove half the total floors at a time.

def binary_search(arr, target):

    # Your code here
    bottom = 0
    top = len(arr) - 1

    while bottom <= top:
        mid = (bottom + top) // 2

        if arr[mid] < target:
            bottom = mid + 1

        elif arr[mid] > target:
            top = mid - 1

        else:
            return mid

    return -1 

Since we are using binary search, the time complexity should be O(log(n))

Answer: O(log(n))

