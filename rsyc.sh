#!/bin/bash
set -x

# DST_DIR="yli922@dusky.sharcnet.ca:/project/ctb-ilie/yli922/pssm/"
DST_DIR="ubuntu@199.241.167.236:/work2/DELPHI_Server/workspace/sites_conservation/"
# DST_DIR="yli922@dusky.sharcnet.ca:/project/ctb-ilie/yli922/sites_conserveravtion/"
SRC_DIR=~/Documents/sites_conserveravtion/*
# mkdir -p $DST_DIR


rsync -r -l -K --progress $SRC_DIR $DST_DIR --exclude ".git" --exclude ".DS_Store" --exclude "dataset/"
echo done
