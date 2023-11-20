import argparse
import json
import sys

def flatten_json(json_obj, parent_key='', sep='.'):
    flattened = {}
    for key, value in json_obj.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key

        if isinstance(value, dict):
            flattened.update(flatten_json(value, new_key, sep=sep))
        else:
            flattened[new_key] = value

    return flattened

def gron(file_path, options):
    try:
        if file_path:
            with open(file_path, 'r') as file:
                json_obj = json.load(file)
        else:
            json_obj = json.load(sys.stdin)

        if options.obj:
            base_object_name = options.obj
        else:
            base_object_name = 'json'

        flattened = flatten_json(json_obj)

        for key, value in flattened.items():
            print(f"{base_object_name}{key} = {value}")

    except json.JSONDecodeError:
        print(f"gron: {file_path}: Unable to parse JSON", file=sys.stderr)
        sys.exit(1)

    except FileNotFoundError:
        print(f"gron: {file_path}: No such file or directory", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="JSON flattener (gron)")
    parser.add_argument('file', nargs='?', help='Input JSON file (optional, if not provided, read from STDIN)')
    parser.add_argument('--obj', help='Specify a base object name')

    options = parser.parse_args()

    gron(options.file, options)

if __name__ == "__main__":
    main()
