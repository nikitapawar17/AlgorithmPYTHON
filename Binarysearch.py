from util.util_class import binary_search


def main():

    arr = [23, 44, 66, 91, 100]
    first = 0
    last = len(arr)-1
    x = 91
    res = binary_search(arr, first, last, x)

    if res != -1:
        print("Searched element at index ", res)
    else:
        print("Element not present ")


if __name__ == main():
    main()
