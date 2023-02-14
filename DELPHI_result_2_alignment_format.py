import os
import sys

dic_pid_2_alignment = {}
def load_alignment_dic(alignment_fn):
    
    fin = open(alignment_fn, "r")
    while True:
        line_pid = fin.readline().rstrip()
        line_alignment = fin.readline().rstrip()
        if not line_alignment:
            break
        dic_pid_2_alignment[line_pid] = line_alignment
    fin.close()

def convert(input_fn, output_fn, pid):
    index = 1
    fin = open(input_fn, "r")
    fout = open(output_fn, "w")
    fout.write("site\ttaxa_count\tDELPHI_score\n")

    alignment = dic_pid_2_alignment[pid]
    for i in alignment:
        if(i == '-'):
            fout.write(str(index)+"\t"+"-"+"\t"+"-"+"\n")
        else:
            line = fin.readline().rstrip()
            fout.write(str(index)+"\t"+"-"+"\t"+line+"\n")  
        index += 1

    fin.close()
    fout.close()

def main():
    input_DELPHI_result_fn = sys.argv[1]
    output_fn = sys.argv[2]
    pid = sys.argv[3]
    alignment_fn = sys.argv[4]
    load_alignment_dic(alignment_fn)
    # print("input_DELPHI_result_fn: ", input_DELPHI_result_fn)
    # print("pid: ", pid)
    # print("output_fn: ", output_fn)
    convert(input_DELPHI_result_fn, output_fn, pid)

if __name__ == '__main__':
    main()

