# Bioinformatics 2 - Jagiellonian University

This repository contains assignments and solutions for the "Bioinformatics 2" course (Academic Year 2025/2026) at Jagiellonian University.

-----

## 📂 Repository Contents

This repository is organized by exercise number.
* **Exercise 1: Jupyter Notebook Introduction**
    * Foundational exercise introduces the Jupyter Notebook environment
    * Covers the basics of the interface, how to create and execute code cells, and how to format text and notes using Markdown cells.
* **Exercise 2: Blast, Polars and Matplotlib**
    * Focuses on performing sequence similarity searches using BLAST
    * Data analyzed using the Polars DataFrame library.
    * Matplotlib is used to create plots and visualize the findings from the alignment data.
* **Exercise 3: Biological Databases**
    * Focuses on accessing PDB, PubMed, Nucleotide, and PubChem.
    * Includes data parsing, chemoinformatics (RDKit), TF-IDF, and PCA.

-----

## 🔬 Biological Databases

This set of exercises focuses on programmatically accessing, parsing, and analyzing data from major biological databases using Python.

**Key topics covered:**

  * **Protein Data Bank (PDB):**

      * Downloading `.pdb` files (e.g., `1UBQ`) via `urllib`.
      * Parsing atom coordinates to calculate geometric distances between atoms.

  * **PubMed (NCBI E-utils):**

      * Using `esearch` to find publication IDs (PMIDs) by author.
      * Using `efetch` to retrieve publication details.
      * Parsing XML responses with `lxml` to extract titles, abstracts, and MeSH terms.
      * Aggregating data (e.g., counting word occurrences in abstracts).

  * **Nucleotide (NCBI E-utils):**

      * Retrieving sequence records (`GBSeq_definition`, `GBSeq_sequence`).
      * Writing a function to automatically save downloaded records in the FASTA format.

  * **PubChem & Chemoinformatics:**

      * Querying the PubChem API to retrieve drug properties and SMILES strings from drug names.
      * Using `RDKit` to calculate key physicochemical properties (MolWt, LogP, TPSA, H-Donors/Acceptors).
      * Visualizing 2D molecule structures from SMILES strings.

  * **Data Analysis:**

      * Applying **TF-IDF** (Term Frequency-Inverse Document Frequency) to vectorize text data (MeSH terms).
      * Using **PCA** (Principal Component Analysis) with `scikit-learn` for dimensionality reduction.
      * Visualizing data clusters (e.g., drug groups vs. other compounds) with `matplotlib`.

-----

## 🛠️ Technologies Used

  * **Core Language:** Python 3
  * **Environment:** Jupyter Notebook
  * **Data Fetching:** `urllib`, `requests`
  * **Parsing:** `lxml` (for XML)
  * **Chemoinformatics:** `rdkit`
  * **Data Analysis:** `pandas`, `scikit-learn` (StandardScaler, PCA)
  * **Visualization:** `matplotlib`