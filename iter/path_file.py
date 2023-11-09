import pathlib


def analyze_data(file: str):
    while True:
        try:
            data = pathlib.Path(file).read_text()
            # analyze the data
        except FileNotFoundError:
            print(f'Does not exist, exiting: {file}')
        except IsADirectoryError:
            print(f'Does not exist directory, dir: {file}')
        except Exception as e:
            raise e


analyze_data('/home/diego/Documentos/N+1.txt')


def your_options():
    path = pathlib.Path("/home/diego/Documentos")
    # path.exists() -> os.path.exists(path)
    # path.is_file() -> os.path.isfile(path)
    # path.is_dir() -> os.path.isdir(path)
    if path.exists():
        print('Found')
        if path.is_dir():
            print("It's a directory")
        if path.is_file():
            print("It's a file")
    else:
        print('Not found')


your_options()
