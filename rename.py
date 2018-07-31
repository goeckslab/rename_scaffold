"""
Call rename to rename scaffolds in target genome so that the sequence names are less than 31 characters. Rename all scaffolds to scaffold_1, scaffold_2, ..., scaffold_N and provide a name mapping file
Call truncate to truncate the scaffold names that are more than 31 characters. Replace each invalid character (non-ASCII, '\t', '\n', '\x0b', '\x0c', '\r') with '_'
"""
import sys
import csv
import codecs
import string

def rename(inputfile, outputfile, writer):
    with open(outputfile, 'w') as out:
        with codecs.open(inputfile, 'r', encoding='utf-8') as rf:
            lines = rf.readlines()
            i = 1
            for line in lines:
                if ">" in line:
                    oldname = line[1:].rstrip()
                    newname = "scaffold_" + str(i)
                    line = ">" + newname + "\n"
                    i = i+1
                    writer.writerow([oldname.encode('utf-8'), newname])
                out.write(line)

def truncate(inputFile, outputFile, valid_characters, writer):
    names = []
    with open(outputFile, 'w') as out:
        with codecs.open(inputFile, 'r', encoding='utf-8') as rf:
            lines = rf.readlines()
            for l in lines:
                if ">" in l:
                    print l.encode('utf-8')
                    oldname = l[1:].rstrip()
                    name = substituteNonAscii(oldname, valid_characters)
                    if len(name) > 31:
                        name = name[:31]
                        print "\tTruncate the scaffold name to less than 31 characters: %s" % name
                    if name in names:
                        sys.exit("Name conflict! Name " + name + " already exist.")
                    writer.writerow([oldname.encode('utf-8'), name])
                    names.append(name)
                    l = ">" + name + "\n"
                    print "======================\n"
                out.write(l)

def substituteNonAscii(str, valid_charaters):
    l = []
    for c in str:
        if c not in valid_charaters:
            print "\tSubstitute invalid character %s with _" % c.encode('utf-8')
            c = '_'
        l.append(c)
    return "".join(l)

def main():
    inputfile = str(sys.argv[1])
    manipulate = str(sys.argv[2])
    outputfile = str(sys.argv[3])
    indexfile = str(sys.argv[4])
    csvfile = open(indexfile, 'w')
    writer = csv.writer(csvfile)
    if manipulate == "rename":
        rename(inputfile, outputfile, writer)
    elif manipulate == "truncate":
        valid_characters = string.letters + string.punctuation + string.digits + ' '
        truncate(inputfile, outputfile, valid_characters, writer)

if __name__ == "__main__":
    main()
    

