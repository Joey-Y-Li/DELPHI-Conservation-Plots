import os,glob
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

def get_Shannon_diversity(T_taxa,shannon_score_fn,alignment_fn):
    x_values = []
    y_values = []
    fin = open(shannon_score_fn, "r")
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
            else:
                x_values.append(site_index)
                y_values.append(float("nan"))
        line_num += 1
    fin.close()
    return x_values, y_values

def normalized(input_array):
    input_array_np = np.asarray(input_array)
    max_Feature = np.nanmax(input_array_np)
    min_Feature = np.nanmin(input_array_np)
    print("max_Feature: ", max_Feature)
    print("min_Feature: ", min_Feature)
    normolized_array = (input_array_np - min_Feature) / (max_Feature - min_Feature)
    return normolized_array
def plot_conservation(T_taxa,conservation_score_fn,alignment_fn, shannon_score_fn, dataset_name, num_pro, len_alignment, gene_name):
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
            else:
                x_values.append(site_index)
                y_values.append(float("nan"))
        line_num += 1
    fin.close()
    # print("x_values: ",x_values)
    # print("y_values: ",y_values)

    plot_width = 38/700 * len_alignment
    fig, ax = plt.subplots(figsize=(plot_width,5))
    plt.ylim(-0.1,1.1)
    plt.xlim(30, len_alignment)
    plt.plot(x_values, y_values, 'b.', label='conservation score')

    ####################
    #plot shannon's diversity
    ####################
    shannon_x_values,shannon_y_values= get_Shannon_diversity(T_taxa,shannon_score_fn,alignment_fn)
    shannon_y_values_normalized = normalized(shannon_y_values)
    # plt.plot(shannon_x_values, shannon_y_values_normalized, 'r.', label="Shannon's diversity")


    ####################
    #load alignment dic
    ####################
    dic_pid_2_alignment = load_alignment_dic(alignment_fn)


    ####################
    #plot DELPHI  consensus results
    ####################
    y_values = np.empty((num_pro,len_alignment))
    cordinat_dir = "plot_cordinates/"+dataset_name
    os.chdir(cordinat_dir)
    index = 0
    for file in glob.glob("?P*.npy"):
        print(file)
        # print("index: ",index)
        temp_y_values_one_protein = np.load(file)
        y_values[index] = temp_y_values_one_protein
        # print("y_values[index]: ",y_values[index])
        index +=1

    delphi_y_values_mean = np.nanmean(y_values, axis = 0)
    delphi_y_values_std = np.nanstd(y_values, axis = 0)
    # print("x_values: ",x_values)
    # print("delphi_y_values_mean: ",delphi_y_values_mean)
    # print("delphi_y_values_std: ",delphi_y_values_std)

    plt.errorbar(x=x_values,y=delphi_y_values_mean,yerr=delphi_y_values_std,marker='^',markersize=1,elinewidth='1',markeredgecolor="green",label="DELPHI consensus", color="orange")


    # delphi_x_values, delphi_y_values = get_delphi_values(x_values, DELPHI_result_fn, dic_pid_2_alignment,pid)
    # plt.plot(delphi_x_values, delphi_y_values, 'g<', label='DELPHI result')
    # np.save("plot_cordinates/delphi_x_values.npy", delphi_x_values)
    # np.save("plot_cordinates/"+pid+".npy", delphi_y_values)
    os.chdir("../../")
    if (gene_name =="SH2"):
        plt.legend(loc='center left')
    else:
        plt.legend()
    if (gene_name =="hemoglobin_top178"):
        plot_title = "Alpha haemoglobin"
    elif (gene_name =="SRY"):
        plot_title = "SRY"
    elif (gene_name =="SH2"):
        plot_title = "SH2D2A"
    else:
        plot_title = gene_name
    plt.title(plot_title)
    plt.xlabel('Amino acid residue index')
    plt.ylabel('Scores')
    plt.savefig("plot_consensus/"+dataset_name+"/"+dataset_name+"_conservation.pdf")
    plt.close()
    



def main():
    # the mininum number of taxa in the alignments to be considered as a site
    T_taxa = int(sys.argv[1])
    conservation_score_fn = sys.argv[2]
    alignment_fn = sys.argv[3]
    shannon_score_fn = sys.argv[4]
    dataset_name = sys.argv[5]
    num_pro = int(sys.argv[6])
    len_alignment = int(sys.argv[7])
    gene_name = sys.argv[8]
    # pid=sys.argv[4]
    # DELPHI_result_fn = sys.argv[5]
    print("T_taxa: ", T_taxa)
    print("conservation_score_fn: ", conservation_score_fn)
    print("alignment_fn: ", alignment_fn)
    # print("pid: ", pid)
    # print("DELPHI_result_fn: ", DELPHI_result_fn)
    plot_conservation(T_taxa,conservation_score_fn,alignment_fn,shannon_score_fn, dataset_name, num_pro, len_alignment, gene_name)

if __name__ == '__main__':
    main()

