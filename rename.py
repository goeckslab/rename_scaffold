"""
Call rename to rename scaffolds in reference genome so that the sequence names are less than 31 characters. Rename all scaffolds to scaffold_1, scaffold_2, ..., scaffold_N and provide a name mapping file
"""
import sys
import csv
from collections import OrderedDict

def rename(inputfile, outputfile, writer):
    namemap = OrderedDict()
    with open(outputfile, 'w') as out:
        with open(inputfile, 'r') as rf:
            lines = rf.readlines()
            i = 1
            for line in lines:
                if ">" in line:
                    oldname = line[1:].rstrip()
                    newname = "scaffold_" + str(i)
                    line = ">" + newname
                    i = i+1
                    writer.writerow([oldname, newname])
                #TODO: Add line breaks to chromosome sequences that are in a single line
                out.write(line.rstrip() + "\n")

def main():
    inputfile = str(sys.argv[1])
    outputfile = str(sys.argv[2])
    indexfile = str(sys.argv[3])
    csvfile = open(indexfile, 'w')
    fieldnames = ['Original sequence name', 'Renamed sequence name']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    rename(inputfile, outputfile, writer)

if __name__ == "__main__":
    main()
    

