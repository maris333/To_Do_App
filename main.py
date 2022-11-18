def to_do_list():
    return []


def add_to_list(to_do_list, item):
    to_do_list.append(item)


def remove_from_list(to_do_list, item):
    pass


def update_entry(to_do_list, item):
    pass


def display_list(to_do_list):
    pass


if __name__ == '__main__':
    my_list = to_do_list()
    add_to_list(my_list, "item1")
    add_to_list(my_list, "item2")
    for item in my_list:
        print(item)



