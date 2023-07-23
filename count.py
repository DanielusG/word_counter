from counter import Counter
import os
import sys
import argparse


def list_files(path):
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            files.append(os.path.join(dirpath, filename))
    return files

def count(args: argparse.Namespace):
    # get all files in current directory recursively
    files = list_files(args.path)

    # count chars in all files
    counterFiles: list[Counter] = []

    print(f'Counting {"lines" if args.line_count else "chars"} in {len(files)} files...')
    for file in files:
        counterFiles.append(Counter(file, args.line_count))

    # count chars in all files
    for counterFile in counterFiles:
        counterFile.analyze()

    # print results
    totalCount = 0
    for counterFile in counterFiles:
        totalCount += counterFile.count
        if counterFile.isIgnored:
            if not args.silent:
                print(f'{counterFile.path}: ignored')
        elif counterFile.notAFile:
            if not args.not_a_file:
                print(f'{counterFile.path}: not a file')
        else:
            print(f'{counterFile.path}: {counterFile.count}')

    print(f'Total: {totalCount}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Count chars in all files in a directory.')
    parser.add_argument('path', metavar='path', type=str, help='path to directory')
    parser.add_argument('-s', '--silent', action='store_true', help='don\'t print ignored files')
    parser.add_argument('-n', '--not-a-file', action='store_true', help='don\'t print not a file files')
    parser.add_argument('-l', '--line-count', action='store_true', help='count lines instead of chars')
    args = parser.parse_args()


    count(args)