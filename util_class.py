import numpy as np

import math

# Anagram string


def is_anagram(str1, str2):
    n1 = len(str1)
    n2 = len(str2)

    if n1 != n2:
        return 0

    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(0, n1):
        if str1[i] != str2[i]:
            return 0
    else:
        return 1

#################################################################################################################

# Prime number


def prime_number(Num):
    for Num in range(1, 1000):
        count = 0
        for j in range(2, (Num // 2 + 1)):
            if Num % j == 0:
                count = count + 1
                break
        if count == 0 and Num != 1:
            print(Num)

#################################################################################################################


# Binary Search
def binary_search(arr, first, last, x):
    while first <= last:

        mid = (first+last) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            first = mid + 1

        else:
            last = mid - 1

    return -1

#################################################################################################################

# Merge Sort


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Check if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Print the list
def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


##################################################################################################################

# convert to binary


def to_binary(str1):
    while len(str1) != 8:
        str1 = "0" + str1
    print("binary number after padding:", str1)
    mid = len(str1) / 2
    part1 = str1[:int(mid)]
    part2 = str1[int(mid):]
    print("part1:", part1)
    print("part2:", part2)
    new_str = part2 + part1
    print("after padding:", new_str)
    new_no = int(new_str, 2)
    print("new number is", new_no)
    if isPowerOfTwo(new_no):
        print(new_no, "is power of two\n")
    else:
        print(new_no, "is not a power of 2 \n")

############################################################################################################

def isPowerOfTwo(new_no):
    return new_no != 0 and ((new_no & (new_no - 1)) == 0)
############################################################################################################

# Insertion Sort


def insertion_sort(arr):

    for i in range(len(arr)):
        d = i
        while d > 0 and arr[d-1] > arr[d]:
            temp = arr[d]
            arr[d] = arr[d-1]
            arr[d-1] = temp
            d -= 1
    return arr

############################################################################################################

# Bubble sort


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

############################################################################################################

# Temp conversion from celsius to fahrenheit


def cel_to_fah(c):
    f = (c * 9 / 5) + 32
    return f

##########################################################################################################

# Temp conversion from fahrenheit to celsius


def fah_to_cel(f):
    c = (f - 32) * 5 / 9
    return c

#############################################################################################################

# Calculate monthly payment


def monthly_payment(P, Y, R):
    n = 12 * Y
    r = R / (12 * 100)
    payment = P * r / 1-pow((1+r), (-n))
    return payment

##############################################################################################################

# calculate sqrt of non-negative no using newton's formula


def sqrt(c):
    t = c
    epsilon = 1 * math.e - 15
    while abs(t - c) / t > epsilon * t:
        t = (c / t + t)/2
        return abs(t)

##########################################################################################################
# vending machine


def vending_machine(change):
    arr = (2000, 500, 200, 100, 50, 20, 10, 5, 2, 1)
    for i in arr:
        if change == 0:
            return 0
        elif change >= i:
            print(i)
            change = vending_machine(change-i)


###########################################################################################################

# Print Days of week


def day_of_week(d, m, y):
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + 31 * m0 // 12) % 7
    print("Day :",d, "Month:",m, "Year:",y)
    return d0

############################################################################################################

# swapping nibbles


def swap_nibbles(x):
    return (x & 0x0f) << 4 | (x & 0xf0) >> 4



#############################################################################################################