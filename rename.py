"""
Call rename to rename scaffolds in reference genome so that the sequence names are less than 31 characters. Rename all scaffolds to scaffold_1, scaffold_2, ..., scaffold_N and provide a name mapping file
"""
import sys
import csv

def rename(inputfile, outputfile, writer):
    with open(outputfile, 'w') as out:
        with open(inputfile, 'r') as rf:
            lines = rf.readlines()
            i = 1
            for line in lines:
                if ">" in line:
                    oldname = line[1:].rstrip()
                    newname = "scaffold_" + str(i)
                    line = ">" + newname + "\n"
                    i = i+1
                    writer.writerow([oldname, newname])
                out.write(line)

def main():
    inputfile = str(sys.argv[1])
    outputfile = str(sys.argv[2])
    indexfile = str(sys.argv[3])
    csvfile = open(indexfile, 'w')
    writer = csv.writer(csvfile)
    rename(inputfile, outputfile, writer)

if __name__ == "__main__":
    main()
    

