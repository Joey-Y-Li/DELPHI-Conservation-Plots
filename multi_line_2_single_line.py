import os
import sys
# this file convers the alignment results from multiple line to single line
def convert(input_fn, output_fn):
    index = 0
    fin = open(input_fn, "r")
    fout = open(output_fn, "w")
    lines = fin.readlines()
    for line in lines:
        if (line[0] == ">"):
            index += 1
            if(index != 1):
                fout.write("\n")    
            fout.write(line.rstrip().split(" ")[0]+"\n")
        
            
        else:
            fout.write(line.rstrip())
            

    fin.close()
    fout.close()

def main():
    input_fn = sys.argv[1]
    output_fn = sys.argv[2]

    convert(input_fn, output_fn)

if __name__ == '__main__':
    main()

