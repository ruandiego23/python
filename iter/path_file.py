import pathlib


def analyze_data(file: str):
    try:
        data = pathlib.Path(file).read_text()
        # analyze the data
    except FileNotFoundError:
        print(f'Does not exist, exiting: {file}')
    except IsADirectoryError:
        print(f'Does not exist directory, dir: {file}')
    else:
        print(data)


analyze_data('/home/diego/Documentos/N+1.txt')


def your_options():
    path = pathlib.Path("path", "to", "some", "file.txt")
    # path.exists() -> os.path.exists(path)
    # path.is_file() -> os.path.isfile(path)
    # path.is_dir() -> os.path.isdir(path)
    if path.exists():
        print('Found')
    else:
        print('Not found')


your_options()
