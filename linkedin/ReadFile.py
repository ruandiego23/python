

def readFile():
    file = open('New.txt', 'r')
    if (file.mode == 'r'):
        content = file.read()
        print(content)

    file.close()


def readBigFile():
    file = open('New.txt', 'r')
    if (file.mode == 'r'):
        content_full = file.readlines()

        for content in content_full:
            print(content)

    file.close()


readBigFile()
readFile()
