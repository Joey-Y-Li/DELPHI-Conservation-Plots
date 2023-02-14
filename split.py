import os
import sys

def split(input_fn, output_dir):
    index = 0
    fin = open(input_fn, "r")
    lines = fin.readlines()
    for line in lines:
        if (line[0] == ">"):
            index += 1
            # if(index != 1):
            #     fout.write("\n")    
            fout = open(output_dir+str(index) + ".fasta", "a+")
            fout.write(line.rstrip().split(" ")[0]+"\n")
            fout.close()
            
        else:
            fout = open(output_dir+str(index) + ".fasta", "a+")
            fout.write(line.rstrip())
            fout.close()

    fin.close()

def main():
    input_fn = sys.argv[1]

    output_dir = sys.argv[2]
    split(input_fn, output_dir)

if __name__ == '__main__':
    main()

