"""
Call rename to rename scaffolds in reference genome so that the sequence names are less than 31 characters. Rename all scaffolds to scaffold_1, scaffold_2, ..., scaffold_N and provide a name mapping file
"""
import sys
from collections import OrderedDict

def rename(inputfile, outputfile, indexfile):
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
                    namemap[oldname] = newname
                #TODO: Add line breaks to chromosome sequences that are in a single line
                #else:
                    #if (len(line) > 50):
                        #for 
                out.write(line.rstrip() + "\n")
    with open(indexfile, 'w') as index:
        for k in namemap:
            index.write(k + "\t" + namemap[k] + "\n")

def main():
    inputfile = str(sys.argv[1])
    outputfile = str(sys.argv[2])
    indexfile = str(sys.argv[3])
    rename(inputfile, outputfile, indexfile)

if __name__ == "__main__":
    main()
    

