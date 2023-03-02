import argparse
import sys


parser = argparse.ArgumentParser(
    # add_help=False, formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, max_help_position=40)
)
parser.add_argument('-o', '--output',
                    default='',
                    help='output directory')

known, unknown = parser.parse_known_args()
# parser.add_argument('-f', '--force-remux',
#                     action='store_true',
#                     help='forcing remux to mp4, requires ffmpeg')
# args = parser.parse_args()

print(known)
print(unknown)
print(len(unknown))
# print(args)

exit()

def main():
    if not args.liked and not args.user and not args.bookmarks:
        print('[red]ERROR: you have to use the -l or -u option, see [bold]--help[/bold].[/red]')
        # sys.exit(1)

    if args.liked:
        search = 'likes'
    elif args.bookmarks:
        search = 'favourites'
    elif args.user:
        search = f'channel/{args.user}'




def single_file(arg):
    print(arg)

parser = argparse.ArgumentParser()
parser.set_defaults(func=single_file)



if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)

