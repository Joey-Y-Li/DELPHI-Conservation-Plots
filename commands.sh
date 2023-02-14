#!/bin/bash

# $1: dataset_dir
function pipeline(){
	dataset_name=$1
	num_pro=$2
	len_alignment=$3

	# python3 multi_line_2_single_line.py dataset/${dataset_name}/input.fna dataset/${dataset_name}/input_DELPHI_format.fna

	# python3 split.py dataset/${dataset_name}/input_DELPHI_format.fna dataset/${dataset_name}/
	# convert to DELPHI_result_2_alignment_format
	# python3 multi_line_2_single_line.py dataset/${dataset_name}/input.aln dataset/${dataset_name}/input_reformated.aln
	# for file in $(ls DELPHI_results/${dataset_name}/*.txt)
	# do
	# 	f_basename=$(basename -- "$file")
	# 	file_no_ext=${f_basename%????}
	# 	echo "basename: $f_basename"
	# 	echo "file: $file"
	# 	echo "file_no_ext: ${file_no_ext}"
	# 	python3 DELPHI_result_2_alignment_format.py ${file} DELPHI_results_alignment_format/${dataset_name}/${file_no_ext}.txt ">${file_no_ext}" dataset/${dataset_name}/input_reformated.aln
	# done
	# # plot individual protein and save npy
	# for file in $(ls DELPHI_results/${dataset_name}/*.txt)
	# do
	# 	f_basename=$(basename -- "$file")
	# 	file_no_ext=${f_basename%????}
	# 	python3 plot_individual_protein.py 10 dataset/${dataset_name}/input.cons dataset/${dataset_name}/input_reformated.aln ${file_no_ext} DELPHI_results_alignment_format/${dataset_name}/${file_no_ext}.txt ${dataset_name}
	# done
	python3 plot_shannon.py 10 dataset/${dataset_name}/input.cons dataset/${dataset_name}/input_reformated.aln dataset/${dataset_name}/input.diversity ${dataset_name} ${num_pro} ${len_alignment} ${dataset_name}
}

pipeline hemoglobin_top178 178 308 
pipeline SRY 40 380
pipeline hemoglobin_top99 99 192
pipeline SH2 66 731


# DELPHI_result_2_alignment_format.py
# for file in $(ls DELPHI_results/*.txt)
# do
# 	f_basename=$(basename -- "$file")
# 	file_no_ext=${f_basename%????}
# 	echo "basename: $f_basename"
# 	echo "file: $file"
# 	echo "file_no_ext: ${file_no_ext}"
# 	python DELPHI_result_2_alignment_format.py ${file} DELPHI_results_alignment_format/${file_no_ext}.txt ">${file_no_ext}"
# done



# plot_individual_protein.py
# for file in $(ls DELPHI_results/*.txt)
# do
# 	f_basename=$(basename -- "$file")
# 	file_no_ext=${f_basename%????}
# 	python plot_individual_protein.py 10 sh2.cons sh24_reformatted.aln ${file_no_ext} DELPHI_results_alignment_format/${file_no_ext}.txt
# done

#plot_consensus.py
# python plot_consensus.py 10 sh2.cons sh24_reformatted.aln


#plot_shannon.py
# python3 plot_shannon.py 10 sh2.cons sh24_reformatted.aln sh2_diversity.txt
