from util.util_class import monthly_payment


def main():
    P = 500000
    Y = 2
    R = 6
    print("Payment = ", monthly_payment(P, Y, R))


if __name__ == main():
    main()
