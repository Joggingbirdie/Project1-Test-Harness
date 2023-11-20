import argparse
import sys

def count_words(file_content):
    lines = file_content.split('\n')
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = sum(len(line) for line in lines)
    return num_lines, num_words, num_chars

def wc(file_path, options):
    with open(file_path, 'r') as file:
        file_content = file.read()

    num_lines, num_words, num_chars = count_words(file_content)

    output = f"{num_lines}\t{num_words}\t{num_chars}"

    if options.lines:
        output = f"{num_lines}"
    elif options.words:
        output = f"{num_words}"
    elif options.characters:
        output = f"{num_chars}"

    print(output)

def main():
    parser = argparse.ArgumentParser(description="Word count utility (wc)")
    parser.add_argument('files', nargs='*', help='Input file(s)')
    parser.add_argument('-l', '--lines', action='store_true', help='Count lines only')
    parser.add_argument('-w', '--words', action='store_true', help='Count words only')
    parser.add_argument('-c', '--characters', action='store_true', help='Count characters only')

    options = parser.parse_args()

    if not options.lines and not options.words and not options.characters:
        options.lines = options.words = options.characters = True

    total_lines, total_words, total_chars = 0, 0, 0

    for file_path in options.files:
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
                num_lines, num_words, num_chars = count_words(file_content)

                total_lines += num_lines
                total_words += num_words
                total_chars += num_chars

                print(f"{num_lines}\t{num_words}\t{num_chars}\t{file_path}")

        except FileNotFoundError:
            print(f"wc: {file_path}: No such file or directory", file=sys.stderr)
            sys.exit(1)

    if len(options.files) > 1:
        print(f"{total_lines}\t{total_words}\t{total_chars}\ttotal")

if __name__ == "__main__":
    main()