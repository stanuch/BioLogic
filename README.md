<p align="center">
  <img src="assets/uj_logo.png" width="400" alt="Jagiellonian University Logo">
</p>

This repository contains implementations of algorithms, data pipelines, and analysis tools developed during the **Bioinformatics 2** curriculum at the Faculty of Biochemistry, Biophysics and Biotechnology, Jagiellonian University. The focus is on the mathematical implementation of biological algorithms and efficient data processing

![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange?logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-Studio-276DC3?logo=r&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Table of Contents

- [Overview](#overview)
- [Project Modules](#project-modules)
- [Data Engineering and Chemoinformatics](#data-engineering-and-chemoinformatics)
- [Genomics and Sequence Analysis](#genomics-and-sequence-analysis)
- [Structural Bioinformatics](#structural-bioinformatics)
- [Technical Stack](#technical-stack)
- [Disclaimer and Missing Data Files](#disclaimer-and-missing-data-files)
- [License](#license)

## Overview

A major component of the coursework involved the prediction and mathematical validation of macromolecular structures. This includes an implementation of the Nussinov algorithm, which utilizes dynamic programming for RNA secondary structure prediction based on base-pair maximization.

To validate structural models, the Kabsch algorithm was implemented using Singular Value Decomposition (SVD) to calculate the Root-Mean-Square Deviation (RMSD) between atomic coordinates. Additionally, the projects utilize the PyMOL API to calculate validation metrics such as TM-scores and GDT_TS. Protein threading was performed using the I-TASSER suite.

## Project Modules

| Module | Topic | Key Techniques |
|--------|-------|----------------|
| [01_Biological_Databases](01_Biological_Databases/) | Data Access & Chemoinformatics | PDB/PubChem/NCBI APIs, TF-IDF, RDKit |
| [02_Sequence_Analysis](02_Sequence_Analysis/) | Sequence Alignment & Visualization | BLAST, Polars, Matplotlib |
| [03_Genome_Analysis](03_Genome_Analysis/) | Restriction Site Analysis | Biopython, E. coli genome |
| [04_Genome_Assembly](04_Genome_Assembly/) | De Novo Assembly | De Bruijn graphs, k-mers |
| [05_Protein_Domains](05_Protein_Domains/) | Domain Architecture | PyHMMER, Pfam, HMM profiles |
| [06_Protein_Structure_Prediction](06_Protein_Structure_Prediction/) | Structure Modeling | I-TASSER, AlphaFold 2/3 |
| [07_Structure_Validation](07_Structure_Validation/) | Model Quality Assessment | Kabsch algorithm, RMSD, TM-score |
| [08_RNA_Structure](08_RNA_Structure/) | Secondary Structure Prediction | Nussinov algorithm, Dynamic Programming |
| [09_scRNA_Seq](09_scRNA_Seq/) | Single-Cell Transcriptomics | R, Seurat-style analysis |
| [10_Crystallography](10_Crystallography/) | Electron Density Analysis | Crystallographic maps |

## Data Engineering and Chemoinformatics

This section contains scripts for acquiring and processing biological data from public repositories (NCBI E-utils, PDB, PubChem). I used the **Polars** library to handle larger datasets more efficiently than standard Pandas.

The work also includes:
* **NLP techniques:** Applying TF-IDF vectorization to scientific literature for MeSH term analysis.
* **Chemoinformatics:** Using **RDKit** to compute physicochemical properties and visualize molecular structures.

## Genomics and Sequence Analysis

Projects focused on understanding genome assembly logic. I implemented **De Bruijn graphs** to demonstrate how short sequencing reads are processed into contigs.

For protein domain analysis, I used **PyHMMER** to query the Pfam database. This involved applying Hidden Markov Models (HMMs) and statistical filtering (E-values, sequence coverage) to correctly identify domain architectures.

## Structural Bioinformatics

This part covers the prediction and validation of macromolecular structures, including protein threading (I-TASSER) and a custom implementation of the **Nussinov algorithm** for RNA secondary structure prediction.

To validate structural models, I implemented the **Kabsch algorithm** using **Singular Value Decomposition (SVD)** to calculate RMSD between atomic coordinates. Additionally, I utilized the **PyMOL API** to compute TM-scores and GDT_TS for comparing predicted models against experimental data.

## Technical Stack

| Category | Tools |
|----------|-------|
| **Data Analysis** | Polars, NumPy, SciPy, Scikit-learn |
| **Bioinformatics** | Biopython, PyHMMER, RDKit, ViennaRNA |
| **Structural Tools** | PyMOL API, I-TASSER, AlphaFold |
| **Visualization** | Matplotlib, Seaborn |
| **Environment** | Jupyter Notebooks, R Markdown |

## Disclaimer and Missing Data Files

> [!WARNING]
>
> This repository has been reorganized from its original academic structure into a thematic portfolio. As a result, some relative file paths inside the notebooks (`.ipynb`) and scripts (`.py`) may reference directories that have been moved or renamed.
>
> While this might prevent some scripts from executing "out of the box" without path adjustments, the logic, implementation details, and code structure remain fully intact.

Some large data files are excluded from this repository. Each module's README contains instructions for obtaining necessary files. Key exclusions:

| File | Module | Source |
|------|--------|--------|
| `e_coli.fasta` | 03_Genome_Analysis | [NCBI](https://www.ncbi.nlm.nih.gov/) |
| Protein FASTAs | 05_Protein_Domains | UniProt batch download |
| `*.cif` files | 06_Protein_Structure_Prediction | [AlphaFold](https://alphafoldserver.com/) and [I-TASSER](https://aideepmed.com/I-TASSER/) |
| scRNA data | 09_scRNA_Seq | Course materials |
| `*.map` files | 10_Crystallography | PDB electron density server |

## License

This repository is licensed under the **MIT License**. You are free to use, modify, and distribute the code.

> **Note**: Some instructional materials are based on course content provided by faculty instructors and may be subject to their original copyright. All original code, analysis, and documentation created by me are freely available under the MIT License.
---
*Maintained by Aleksander Stanuch as part of the Faculty of Biochemistry, Biophysics and Biotechnology curriculum at Jagiellonian University.*
