from PDFIndexer.index import add_index, add_index_offset, show_tree, read_index
import argparse
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, required=True)
parser.add_argument("-o", "--output", type=str, required=True)
parser.add_argument("-I", "--index", type=str, required=True)
parser.add_argument("-O", "--offset", type=int)
parser.add_argument("-v", "--verbose", action="store_true")

args = parser.parse_args()
input_file = args.input
output_file = args.output
index_file = args.index

if not input_file:
    print("No input file specified")
    sys.exit(1)

if not output_file:
    print("No output file specified")
    sys.exit(1)

if not args.index:
    print("No index file specified")
    sys.exit(1)

if not os.path.exists(input_file):
    print("Input file does not exist")
    sys.exit(1)

if not os.path.exists(index_file):
    print("Index file does not exist")
    sys.exit(1)

index = read_index(index_file)

if args.offset:
    index = add_index_offset(index, args.offset)

if args.verbose:
    print(index)
    show_tree(index)

add_index(input_file, output_file, index)
