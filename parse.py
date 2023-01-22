#!/bin/python3
import re

with open("silcawl.txt") as fin:
	with open("silcawl.csv", "w") as fout:
		print("ID\tCATEGORY\t\t\t\tWORD", file=fout)
		in_header = False
		curr_header = ""
		num_header = [0, 0, 0]
		
		for line in fin:
			splitline = re.split(r"\s{2,}", line)
			
			# Ignore empty lines
			if line == '\n':
				continue
			# If line is a category header
			elif "." in splitline[0]:
				# Append to header string if content hasn't started yet
				if in_header:
					curr_header += ' ' + splitline[1]
				# Otherwise, reset header string
				else:
					curr_header = splitline[1]
					# Get category number
					dot_split = line.split(".")
					
					num_header[0] = int(dot_split[0])
					
					m = re.search(r"(?<=\.)\d+", line)
					
					if m != None:
						num_header[1] = int(m.group(0))
						if m.lastindex != None:
							num_header[2] = int(m.group(1))
						else:
							num_header[2] = 0
					else:
						num_header[1] = 0
				in_header = True
			else:
				print("{}\t{}\t{}\t{}\t{}\t{}".format(
					splitline[0],
					curr_header,
					num_header[0],
					num_header[1],
					num_header[2],
					splitline[1]
				), file=fout)
				in_header = False
