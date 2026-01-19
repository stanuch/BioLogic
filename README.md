<p align="center">
  <img src="img/uj_logo.png" width="400" alt="Jagiellonian University Logo">
</p>

# <p align="center">Bioinformatics</p>

This repository contains implementations of algorithms, data pipelines, and analysis tools developed during the **Bioinformatics 2** curriculum at the Faculty of Biochemistry, Biophysics and Biotechnology, Jagiellonian University. The focus is on the mathematical implementation of biological algorithms and efficient data processing

---

### Academic Objectives and Methodology

A major component of the coursework involved the prediction and mathematical validation of macromolecular structures. This includes an implementation of the Nussinov algorithm, which utilizes dynamic programming for RNA secondary structure prediction based on base-pair maximization.

To validate structural models, the Kabsch algorithm was implemented using Singular Value Decomposition (SVD) to calculate the Root-Mean-Square Deviation (RMSD) between atomic coordinates. Additionally, the projects utilize the PyMOL API to calculate validation metrics such as TM-scores and GDT_TS. Protein threading was performed using the I-TASSER suite.

### Data Engineering and Chemoinformatics

This repository contains automated pipelines designed to acquire and process data from public repositories, including NCBI E-utils, the Protein Data Bank (PDB), and PubChem. To handle large datasets efficiently, the Polars library was used for data manipulation, prioritizing memory management over traditional processing frameworks.

The work also includes Natural Language Processing techniques, specifically TF-IDF vectorization, applied to scientific literature for MeSH term analysis. In the field of chemoinformatics, RDKit was utilized to compute physicochemical properties and to generate visualizations of molecular structures.

### Genomics and Sequence Analysis

The projects in this section explore the logic behind de novo genome assembly. Specifically, the code implements De Bruijn graphs to demonstrate how short sequencing reads are processed into continuous contigs.

Furthermore, protein domain analysis was conducted using PyHMMER to query the Pfam database. This work involved the application of Hidden Markov Models (HMMs) to identify domain architectures. The analysis includes the implementation of statistical filtering, such as iE-values and sequence coverage thresholds, to ensure biological relevance.

### Structural Bioinformatics and Mathematical Validation

The most technically demanding aspect of the course involved the prediction and validation of macromolecular structures. This included protein threading using the **I-TASSER** suite and the implementation of the **Nussinov algorithm** for RNA secondary structure prediction based on base-pair maximization.

To ensure the accuracy of structural models, I implemented the **Kabsch algorithm** using **Singular Value Decomposition (SVD)** to calculate the Root-Mean-Square Deviation (RMSD) between atomic coordinates. This mathematical approach to structural validation was complemented by the use of the PyMOL API to calculate TM-scores and GDT_TS, providing a robust framework for assessing the quality of predicted models against experimental data.

---

### Technical Stack

* **Data Analysis:** Polars, NumPy, SciPy, and Scikit-learn (PCA, StandardScaler)
* **Bioinformatics & Chemistry:** Biopython, PyHMMER, RDKit, AlphaFold and ViennaRNA
* **Structural Tools:** PyMOL API and I-TASSER integration
* **Environment:** Jupyter Notebooks
* **Visualization:** Matplotlib and Seaborn

---
*Maintained by Aleksander Stanuch as part of the Faculty of Biochemistry, Biophysics and Biotechnology curriculum at Jagiellonian University.*