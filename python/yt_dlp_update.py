#!/bin/env python

from pathlib import Path
import subprocess
import re
import sys
import os


regex = re.compile(r"([0-9A-Za-z_-]{11})[\]|\)]?\.[m|w]")


if len(sys.argv) > 1:
    working_path = Path(sys.argv[1])
else:
    working_path = Path('.')


def __run(opts: list):
    subprocess.run(opts)


def dunstify(title: str = 'YouTube Video Updater', text: str = '', priority: str = 'low', id: int = 9999):
    __run(['dunstify', '-u', f'{priority}', '-r', f'{id}', f'{title}', f'{text}'])


def __filter_files() -> list | None:
    files: list = []

    for file in filter(lambda y: y.is_file(), working_path.iterdir()):
        if result := regex.search(str(file)):
            files.append(result.group(1))

    if files:
        return files

    text = "ABORT!NO CORRESPONDING FILES WERE FOUND".split('!')

    dunstify(title=text[0], text=text[1])
    sys.exit(f'{text[0]}\n{text[1]}')


def download():
    files: list = __filter_files()
    length = len(files)
    os.chdir(working_path)

    for count, file in enumerate(files):
        dunstify(text=f'In Progress: {count} of {length}', id=4754)
        __run(['yt-dlp', '--embed-thumbnail', '--embed-chapters', '--embed-subs', '-f mp4', f'https://youtu.be/{file}'])
        dunstify(text=f'Done: {count+1} of {length}', id=4754)

    dunstify(text=f'Stats: {length} file{"s" if length > 1 else ""}', priority='normal', id=4753)


if __name__ == '__main__':
    download()
