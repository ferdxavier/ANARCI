#!/bin/bash
# Run the pipeline to get the sequences, format them and build the databases

echo "INFO: ANARCI lives in: "$(pwd)
echo "INFO: Downloading germlines from IMGT and building HMMs..."
echo "INFO: running 'RUN_pipeline.sh', this will take a couple a minutes."

# Workdir
DIR=$(pwd)/build_pipeline

# Places binaries in processing context
export PATH="$PATH:$(pwd)/bin"

# Rip the sequences from the imgt website. HTML may change in the future. 
mkdir -p $DIR/IMGT_sequence_files/htmlfiles
mkdir -p $DIR/IMGT_sequence_files/fastafiles
python $DIR/RipIMGT.py

# Format the alignments and handle imgt oddities to put into a consistent alignment format
mkdir -p $DIR/curated_alignments
mkdir -p $DIR/muscle_alignments
python $DIR/FormatAlignments.py

# Build the hmms for each species and chain.
# --hand option required otherwise it will delete columns that are mainly gaps. We want 128 columns otherwise ARNACI will fall over.
mkdir -p $DIR/HMMs
hmmbuild --hand $DIR/HMMs/ALL.hmm $DIR/curated_alignments/ALL.stockholm
#hmmbuild --hand $DIR/HMMs/ALL_AND_C.hmm $DIR/curated_alignments/ALL_AND_C.stockholm

# Turn the output HMMs file into a binary form. This is required for hmmscan that is used in ARNACI.
hmmpress -f $DIR/HMMs/ALL.hmm 
#hmmpress -f $DIR/HMMs/ALL_AND_C.hmm

# Copy depends inside 'temp' project
mkdir -p $(pwd)/lib/python/anarci/dat
cp -R $DIR/HMMs/ $(pwd)/lib/python/anarci/dat
cp $DIR/curated_alignments/germlines.py $(pwd)/lib/python/anarci