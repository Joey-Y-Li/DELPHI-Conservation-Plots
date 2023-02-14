#!/bin/bash
set -x
#please modify two directories below to your own directories
SRC_DIR="/Users/joeyli/Documents/sites_conserveravtion/*"
DST_DIR="yli922@graham.computecanada.ca:/project/ctb-ilie/yli922/sites_conserveravtion/"

rsync --progress -r -l -K ${SRC_DIR} ${DST_DIR} --exclude ".DS_Store" --exclude "plot_cordinates/" --exclude "plot_consensus/" --exclude "plot/" --exclude "DELPHI_results_alignment_format/" --exclude "DELPHI_results/"
