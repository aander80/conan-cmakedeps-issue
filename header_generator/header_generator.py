import argparse
import sys

def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("classes", nargs="+")
    parser.add_argument("-o", "--output-file", required=True)
    return parser.parse_args(argv)

def main(argv):
    args = parse_args(argv)
    lines = [f"class {c};\n" for c in args.classes]
    with open(args.output_file, "w") as output_file:
        output_file.writelines(lines)

if __name__ == "__main__":
    main(sys.argv[1:])
