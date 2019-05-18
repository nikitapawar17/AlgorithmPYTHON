from util.util_class import cel_to_fah
from util.util_class import fah_to_cel


def main():
    c = int(input("Enter temp in celsius : "))
    print("Temp convert in fah : ", cel_to_fah(c))

    f = int(input("Enter temp in fah : "))
    print("Temp convert in celsius : ", fah_to_cel(f))


if __name__ == main():
    main()
