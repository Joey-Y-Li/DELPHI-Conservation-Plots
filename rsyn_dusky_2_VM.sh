#!/bin/bash
set -x
#please modify two directories below to your own directories
SRC_DIR="/project/ctb-ilie/yli922/sites_conserveravtion/PSSMs/*"
DST_DIR="ubuntu@199.241.167.236:/work2/DELPHI_Server/PSSM_database/PSSMs/"

rsync --progress -r -l -K ${SRC_DIR} ${DST_DIR} --exclude ".DS_Store" --exclude "plot_cordinates/" --exclude "plot_consensus/" --exclude "plot/" --exclude "DELPHI_results_alignment_format/" --exclude "DELPHI_results/"
