from util.util_class import day_of_week
import sys


def main():

    #day = day_of_week(17, 5, 2019)  Prints default result

    d = int(sys.argv[1])            # Take cmd line parameter & print result
    m = int(sys.argv[2])
    y = int(sys.argv[3])
    print("Value for given day is : ", day_of_week(d, m, y))
    #print(day)


if __name__ == main():
    main()
