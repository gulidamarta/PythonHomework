def sort_names_in_file(filepath_from, filepath_to):
    """Open file in a folder, sort the names and write them in a new file.
    Each name should start from a new line.
    """
    names_list = list()
    with open(filepath_from) as input_file:
        names_list = input_file.readlines()
    names_list.sort()
    with open(filepath_to, 'w') as output_file:
        output_file.writelines(names_list)


def main():
    """Test examples for function sort_names_in_file"""
    sort_names_in_file('data/unsorted_names.txt', 'data/sorted_names.txt')


if __name__ == '__main__':
    main()
