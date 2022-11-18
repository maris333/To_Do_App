def to_do_list():
    return []


def add_to_list(to_do_list, item):
    to_do_list.append(item)


if __name__ == '__main__':
    my_list = to_do_list()
    add_to_list(my_list, "item1")
    add_to_list(my_list, "item2")
    for item in my_list:
        print(item)



