import sys
import json
from functools import reduce

def remove_code(data):
	if (data["cell_type"] == "code"):
		data["outputs"] = []
	return data

def remove_source(data):
	data["source"] = []
	return data 


if __name__ == "__main__":
	in_file_name = sys.argv[1]
	out_file_name = in_file_name.split(".")[0] + ".czysty.ipynb"

	in_file = open(in_file_name, 'r')
	out_file = open(out_file_name, 'w')

	data = json.load(in_file)
	cells = data["cells"]
	
	# removes code
	cells = list(map(remove_code, cells))
 
	# removes source for cells that fit the requirement
	cells = [remove_source(val) if idx in list(reduce(lambda prev, curr: (prev[0] + [curr[0]], curr[1]["cell_type"], curr[1]["source"] + [""]) if (prev[1] == "markdown" and curr[1]["cell_type"] == "code" and "# Ćwiczenie" in prev[2][0]) else (prev[0], curr[1]["cell_type"], curr[1]["source"] + [""]), enumerate(cells), ([], "", "")))[0] else val for idx, val in enumerate(cells)]
	
	data["cells"] = cells
	out_file.write(json.dumps(data))

	in_file.close()
	out_file.close()
 
 