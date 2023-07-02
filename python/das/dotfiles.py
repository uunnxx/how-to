import os.path


filenames = {
    'nvim'
}

def find_dotfiles(dotfile_name):
    return open(f'/home/baka/.{dotfile_name}').read()


print(find_dotfiles('gitignore_global'))
