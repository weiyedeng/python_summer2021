
#%% sorting algorithm I: bubble sort (O(n^2))
import os
from datetime import datetime
import time
import random

def bubble_sort(numbers):
    answer = numbers.copy()
    # We go through the list as many times as there are elements
    for i in range(len(answer)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(answer) - 1):
            if answer[j] > answer[j+1]:
                # Swap
                answer[j], answer[j+1] = answer[j+1], answer[j]
# =============================================================================
#         print(answer)
# =============================================================================
    return answer

#test bubble sort
numbers = [5,9,2,6,7,5,10,12,4,6]
bubble_sort(numbers)

#get the running time
bubble_running_time = []
for i in range(1,501):
    random_numbers = random.sample(range(1,2000),i)
    start_time = time.time()
    bubble_sort(random_numbers)
    bubble_running_time.append(time.time() - start_time)
#%% soring algorithm II: merge sort (O(nlog_2n)) 
# Reference: https://realpython.com/sorting-algorithms-python/
def merge(left, right):
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        
        ## check what merge() is doing!
# =============================================================================
#         print("calling merge():")
#         print(result)
#         
# =============================================================================
        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break  
    return result

# See how merge() behaves
l = [1,8,5,4,10]
r = [2,7,6,3,9]
merge(l,r)

# As shown, merge() can sort a list when there is one element in each sublist - 
# That is, we need to use a function to divide the list and call merge() within that function
# This is what merge_sort() tries to do:
def merge_sort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    
    ## check what merge_sort() is doing!
# =============================================================================
#     print("calling merge_sort():")
#     print(array)
#     
# =============================================================================
    if len(array) < 2:
        return array

    midpoint = len(array) // 2
    left=merge_sort(array[:midpoint])
    right=merge_sort(array[midpoint:])
    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(left, right)

# See how merge_sort() behaves
a = [1,8,5,4,10,2,7,6,3,9]
merge_sort(a)

# "The second step splits the input array recursively and calls merge() for each half. 
# Since the array is halved until a single element remains, 
# the total number of halving operations performed by this function is log2n. 
# Since merge() is called for each half, we get a total runtime of O(n log2n)."

# get the running time
merge_running_time = []
for i in range(1,501):
    random_numbers = random.sample(range(1,2000),i)
    start_time = time.time()
    merge_sort(random_numbers)
    merge_running_time.append(time.time() - start_time)

#%% Plotting 

import math
import matplotlib.pyplot as plt

# The plots are supposed to be:
n = range(1,51)
On2 = [i ** 2 for i in n]
OnLogN = [i * math.log(i) for i in n]
plt.plot(n, OnLogN, 'g-', label = "Supposed O(n Log n )")
plt.plot(n, On2, 'y-', label = "Supposed O(2n)")
plt.title("The Effect of Bubble Sort and Merging Sort Algorithms on Runtime")
plt.legend()
plt.xlabel("N")
plt.ylabel("Unit of Time")
plt.show()

# And it turns out:
m = range(1,501)
On2 = [i ** 2 for i in n]
OnLogN = [i * math.log(i) for i in n]
plt.plot(m,merge_running_time, 'g-', label = "Actual O(n Log n )")
plt.plot(m,bubble_running_time, 'y-', label = "Actual O(2n)")
plt.title("The Effect of Bubble Sort and Merging Sort Algorithms on Runtime")
plt.legend()
plt.xlabel("N")
plt.ylabel("Seconds")
plt.show()

# Quite similar!
