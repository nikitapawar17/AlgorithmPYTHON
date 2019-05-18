from util.util_class import to_binary


try:

    print("enter numbers : ")
    num = int(input())
    str1 = bin(num).replace("0b", "")
    print(str1)
    to_binary(str1)

except RuntimeError:
    print("oops something went wrong\n")


