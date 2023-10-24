import os


def br(delimiter: str = '-', columns: int | None = None) -> None:
    if columns:
        print(f'\n{delimiter * columns}\n')
        return None

    columns = os.get_terminal_size().columns
    print(f'\n{delimiter * columns}\n')


if __name__ == '__main__':
    br()
