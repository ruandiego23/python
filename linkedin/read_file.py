

def read_file():
    file = open('New.txt', 'r')
    if file.mode == 'r':
        content = file.read()
        print(content)

    file.close()
    print()


def read_big_file():
    file = open('New.txt', 'r')
    if file.mode == 'r':
        content_full = file.readlines()

        for content in content_full:
            print(content)

    file.close()
    print()


read_file()
read_big_file()
