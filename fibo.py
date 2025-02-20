import random

def generate_array(size, min_val=1, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] < right[0] else right.pop(0))
    return result + left + right

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[i - 1] + seq[i - 2])
    return seq

def is_palindrome(s):
    return s == s[::-1]

def find_max(arr):
    return max(arr)

def find_min(arr):
    return min(arr)

def sum_array(arr):
    return sum(arr)

def unique_elements(arr):
    return list(set(arr))

def main():
    arr = generate_array(10, 1, 100)
    print("Original Array:", arr)
    print("Quick Sort:", quick_sort(arr[:]))
    print("Merge Sort:", merge_sort(arr[:]))
    print("Max Element:", find_max(arr))
    print("Min Element:", find_min(arr))
    print("Sum of Elements:", sum_array(arr))
    print("Fibonacci Sequence:", fibonacci(10))
    print("Factorial of 5:", factorial(5))
    print("Palindrome Check:", is_palindrome("racecar"))
    print("Unique Elements:", unique_elements(arr))
    print("Binary Search for 5:", binary_search(sorted(arr), 5))

if __name__ == "__main__":
    main()
