from PDFIndexer.index import add_index, add_index_offset, show_tree
import argparse

parser = argparse.ArgumentParser()

args = parser.parse_args()
input = args.input
output = args.output
index = add_index(input)
add_index_offset(index, args.offset)
show_tree(index)
