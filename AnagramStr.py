from util.util_class import is_anagram


def main():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string : ")
    if is_anagram(str1, str2):
        print("Strings are anagram ")
    else:
        print("Strings are not anagram ")


if __name__ == main():
    main()
