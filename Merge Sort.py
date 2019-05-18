from util.util_class import merge_sort
from util.util_class import print_list


def main():
    arr = [45, 77, 12, 99, 56, 89]
    print("Array before sorting : ")
    print_list(arr)
    merge_sort(arr)
    print("Array after sorting : ")
    print_list(arr)


if __name__ == main():
    main()
