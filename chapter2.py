def count_lines(file_name):
    try:
        return len(open(file_name, 'r').readlines())
    except IOError:
        return None

if __name__ == "__main__":
    my_file=input('Enter a file to open: ')
    print(count_lines(my_file))