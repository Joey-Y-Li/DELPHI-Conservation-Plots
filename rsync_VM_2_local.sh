#!/bin/bash
set -x
#please modify two directories below to your own directories
SRC_DIR="ubuntu@199.241.167.236:/work2/DELPHI_Server/workspace/sites_conservation/*"
DST_DIR="/Users/joeyli/Documents/sites_conserveravtion/"

# sshpass -p "LYWsw518514518!" rsync -r -l -K --info=progress2 ${SRC_DIR} ${DST_DIR} --include="/ge_test_train" --include="/ge_test_bbit" --exclude="*"
# rsync -r -l -K ${SRC_DIR} ${DST_DIR}

rsync  -r -l -K ${SRC_DIR} ${DST_DIR}
