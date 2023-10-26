'''
python3 copy_file.py in.txt out.txt
'''

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="file to be read")
parser.add_argument("output_file", help="file to save result")

args = parser.parse_args()

def copy_all_lines(input_file, output_file):
	in_file = open(input_file, "r")
	out_file = open(output_file, "w")
 
	while (line := in_file.readline()):
		out_file.write(line)
  
	in_file.close()
	out_file.close()

copy_all_lines(args.input_file, args.output_file)