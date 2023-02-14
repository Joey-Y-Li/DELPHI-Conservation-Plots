#!/bin/bash

#SBATCH --account=def-<user>  # The account to use
#SBATCH --time=96:00:00       # The duration in HH:MM:SS format of each task in the array
#SBATCH --account=ctb-ilie_cpu
#SBATCH --partition=shadowfax
#SBATCH --cpus-per-task=1     # The number of cores for each task in the array
#SBATCH --mem-per-cpu=30G    # The memory per core for each task in the array
#SBATCH --array=1-40
#SBATCH --output=logs/%j.out
module load nixpkgs/16.09  gcc/5.4.0 blast+/2.6.0
# let id="${SLURM_ARRAY_TASK_ID}+10000"
out_pssm="/project/ctb-ilie/yli922/sites_conserveravtion/PSSMs/SRY_${SLURM_ARRAY_TASK_ID}.pssm"
# if [ ! -f "${out_pssm}" ]; then
#     echo "${out_pssm} not exist, compute it"
psiblast -query dataset/SRY/${SLURM_ARRAY_TASK_ID}.fasta -db /cvmfs/ref.mugqic/genomes/blast_db/nr  -out_ascii_pssm ${out_pssm} -num_iterations 3
# else
#     echo "pssm exists, skip"
# fi

