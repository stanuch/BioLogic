#!/usr/bin/bash

python3 run_alphafold.py \
--fasta_paths=7qvb.fasta \
--max_template_date=2021-12-31 \
--model_preset=multimer \
--output_dir=/data/af2data/output/af2/7qvb_dimer \
--data_dir=/data/af2data \
--uniref90_database_path=/data/af2data/uniref90/uniref90.fasta \
--mgnify_database_path=/data/af2data/mgnify/mgy_clusters.fa \
--template_mmcif_dir=/data/af2data/pdb_mmcif/mmcif_files \
--obsolete_pdbs_path=/data/af2data/pdb_mmcif/obsolete.dat \
--uniclust30_database_path=/data/af2data/uniclust30/uniclust30_2018_08/uniclust30_2018_08 \
--bfd_database_path=/data/af2data/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt \
--use_gpu_relax=True \
--pdb_seqres_database_path=/data/af2data/pdb_seqres/pdb_seqres.txt \
--uniprot_database_path=/data/af2data/uniprot/uniprot.fasta
