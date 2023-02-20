import argparse

def main(filepath):
    # replacement strings
    WINDOWS_LINE_ENDING = b'\r\n'
    UNIX_LINE_ENDING = b'\n'

    with open(filepath, 'rb') as open_file:
        content = open_file.read()
        
    # Windows ➡ Unix
    if args.linux:
        content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

    # Unix ➡ Windows
    if args.windows:
        content = content.replace(UNIX_LINE_ENDING, WINDOWS_LINE_ENDING)

    with open(filepath, 'wb') as open_file:
        open_file.write(content)

if __name__ == "__main__":
  
    duplicates = {}
    # Handle command line input here
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    parser.add_argument('-l', '--linux', action='store_true', help="Change to Linux line endings")
    parser.add_argument('-w', '--windows', action='store_true', help="Change to Windows line endings")
    args = parser.parse_args()
    main(args.filepath)