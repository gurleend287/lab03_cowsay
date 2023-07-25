import sys
import heifer_generator


# lists the names of the cows from the list of cow objects
def _list_cows(cows: list):
    cow_names = []
    for item in cows:
        cow_names.append(item.get_name())
    return cow_names


# finds if the cow object exists given the cow name
def _find_cow(name: str, cows: list):
    for item in cows:
        if name.__eq__(item.get_name()):
            return item
        elif cows.index(item) == (len(cows) - 1):
            return None


def main():
    # prints names of cows available if user input includes -l
    if sys.argv[1].__eq__("-l"):
        print("Cows available: ", end='')
        list = _list_cows(heifer_generator.get_cows())
        print(*list)

    # if user input includes -n
    elif sys.argv[1].__eq__("-n"):
        # sets cow name
        cow_name = sys.argv[2]
        # sets message
        message = sys.argv[3:]
        # if cow name not found in list then print not found statement
        if _find_cow(cow_name, heifer_generator.get_cows()) is None:
            print("Could not find", cow_name, "cow!")
        # else print cow with message
        else:
            cow = _find_cow(cow_name, heifer_generator.get_cows())
            print()
            print(*message)
            print(cow.get_image())

    # default cow if user does not enter -l or -n
    else:
        cow_name = 'heifer'
        message = sys.argv[1:]
        cow = _find_cow(cow_name, heifer_generator.get_cows())
        print()
        print(*message)
        print(cow.get_image())



if __name__ == '__main__':
    main()
