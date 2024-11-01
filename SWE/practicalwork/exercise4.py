import time
import math
import random

def linear_search(arr, target):
    indices = []
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            indices.append(i)
    return indices if indices else -1, comparisons  # Return all indices and comparisons

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons  # Return -1 if target not found, and comparisons

def binary_search_insertion_point(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left  # Insertion point

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    comparisons = 0

    while arr[min(step, n) - 1] < target:
        comparisons += 1
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1, comparisons  # Not found

    while arr[prev] < target:
        comparisons += 1
        prev += 1
        if prev == min(step, n):
            return -1, comparisons  # Not found

    comparisons += 1
    if arr[prev] == target:
        return prev, comparisons  # Found
    
    return -1, comparisons  # Not found

def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result, linear_comparisons = linear_search(arr, target)
    linear_time = time.time() - start_time

    # Binary Search (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result, binary_comparisons = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time

    # Jump Search (on sorted array)
    start_time = time.time()
    jump_result, jump_comparisons = jump_search(arr_sorted, target)
    jump_time = time.time() - start_time

    print(f"Linear Search: Found at indices {linear_result}, Comparisons: {linear_comparisons}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Comparisons: {binary_comparisons}, Time: {binary_time:.6f} seconds")
    print(f"Jump Search: Found at index {jump_result}, Comparisons: {jump_comparisons}, Time: {jump_time:.6f} seconds")

# Test with a larger list
large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)

# Test the insertion point function
test_list_sorted = sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
insertion_point = binary_search_insertion_point(test_list_sorted, 7)
print(f"Binary Search Insertion Point: Insertion point for 7 is at index {insertion_point}")

# Recursive Binary Search (unchanged for comparison purposes)
def binary_search_recursive(arr, target, left, right, comparisons=0):
    if left > right:
        return -1, comparisons
    
    mid = (left + right) // 2
    comparisons += 1
    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, comparisons)
    else:
        return binary_search_recursive(arr, target, left, mid - 1, comparisons)

# Test the recursive function
result, comparisons = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}, Comparisons: {comparisons}")

# Main function for random tests
def main():
    # Create a list of 20 random integers between 1 and 100
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list)  # Choose a random target from the list
    print(f"\nSearching for: {target}")
    
    # Linear Search
    result, comparisons = linear_search(test_list, target)
    print(f"Linear Search: Found at indices {result}, Comparisons: {comparisons}")
    
    # Binary Search (iterative)
    sorted_list = sorted(test_list)
    result, comparisons = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result}, Comparisons: {comparisons}")
    
    # Binary Search (recursive)
    result, comparisons = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (recursive): Found at index {result}, Comparisons: {comparisons}")
    
    # Jump Search
    result, comparisons = jump_search(sorted_list, target)
    print(f"Jump Search: Found at index {result}, Comparisons: {comparisons}")
    
    # Compare performance
    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(100000)), 99999)

if __name__ == "__main__":
    main()
