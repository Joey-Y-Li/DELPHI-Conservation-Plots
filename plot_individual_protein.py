import os
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('pdf')



def load_alignment_dic(alignment_fn):
    dic_pid_2_alignment = {}
    fin = open(alignment_fn, "r")
    while True:
        line_pid = fin.readline().rstrip()
        line_alignment = fin.readline().rstrip()
        if not line_alignment:
            break
        dic_pid_2_alignment[line_pid] = line_alignment
    return dic_pid_2_alignment


def get_delphi_values(x_values, DELPHI_result_fn, dic_pid_2_alignment,pid):
    alignment = dic_pid_2_alignment[">"+pid]
    delphi_x_values = []
    delphi_y_values = []
    fin = open(DELPHI_result_fn, "r")
    lines = fin.readlines()
    line_num = 1
    for line in lines:
        # print (line)
        if(line_num != 1): # skip the first line
            site_index = int(line.rstrip().split()[0])
            # num_taxa = int(line.rstrip().split()[1])
            DELPHI_score = line.rstrip().split()[2]
            # print("site_index: ", site_index)
            # print("num_taxa: ", num_taxa)
            # print("DELPHI_score: ", DELPHI_score)
            if (site_index in x_values and alignment[site_index-1] != '-'):
                # print("site_index: ", site_index)
                # print("alignment: ", alignment)
                delphi_x_values.append(site_index)
                delphi_y_values.append(float(DELPHI_score))
            else:
                delphi_x_values.append(site_index)
                delphi_y_values.append(float('nan'))
        line_num += 1
    fin.close()
    return delphi_x_values,delphi_y_values


def plot_conservation(T_taxa,conservation_score_fn,alignment_fn,pid,DELPHI_result_fn, dataset_name):
    ##################
    #plot conservation
    ##################
    x_values = []
    y_values = []
    fin = open(conservation_score_fn, "r")
    lines = fin.readlines()

    line_num = 1
    for line in lines:
        # print (line)
        if(line_num != 1): # skip the first line
            site_index = int(line.rstrip().split()[0])
            num_taxa = int(line.rstrip().split()[1])
            conservation_score = float(line.rstrip().split()[2])
            # print("site_index: ", site_index)
            # print("num_taxa: ", num_taxa)
            # print("conservation_score: ", conservation_score)
            if (num_taxa > T_taxa):
                x_values.append(site_index)
                y_values.append(conservation_score)
        line_num += 1
    fin.close()
    # print("x_values: ",x_values)
    # print("y_values: ",y_values)

    fig, ax = plt.subplots(figsize=(38,14))
    plt.plot(x_values, y_values, 'b.', label='conservation score')
    ####################
    #load alignment dic
    ####################
    dic_pid_2_alignment = load_alignment_dic(alignment_fn)


    ####################
    #plot DELPHI results
    ####################
    
    delphi_x_values, delphi_y_values = get_delphi_values(x_values, DELPHI_result_fn, dic_pid_2_alignment,pid)
    plt.plot(delphi_x_values, delphi_y_values, 'g<', label='DELPHI result')
    np.save("plot_cordinates/"+dataset_name+"/delphi_x_values.npy", delphi_x_values)
    np.save("plot_cordinates/"+dataset_name+"/"+pid+".npy", delphi_y_values)
    plt.legend()
    plt.title('Comparison between conservation score and DELPHI results on '+ pid)
    plt.xlabel('Amino acid residue index')
    plt.ylabel('Scores')
    plt.savefig("plot/"+dataset_name+"/"+pid+".pdf")
    plt.close()
    



def main():
    # the mininum number of taxa in the alignments to be considered as a site
    T_taxa = int(sys.argv[1])
    conservation_score_fn = sys.argv[2]
    alignment_fn = sys.argv[3]
    pid=sys.argv[4]
    DELPHI_result_fn = sys.argv[5]
    dataset_name = sys.argv[6]
    print("T_taxa: ", T_taxa)
    print("conservation_score_fn: ", conservation_score_fn)
    print("alignment_fn: ", alignment_fn)
    print("pid: ", pid)
    print("DELPHI_result_fn: ", DELPHI_result_fn)
    plot_conservation(T_taxa,conservation_score_fn,alignment_fn,pid,DELPHI_result_fn, dataset_name)

if __name__ == '__main__':
    main()

