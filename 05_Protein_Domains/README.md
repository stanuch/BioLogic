# Protein Domain Analysis

Hidden Markov Model-based domain identification using PyHMMER and Pfam.

## Topics Covered

- **PyHMMER**: Python bindings for HMMER3 suite
- **Pfam Database**: Protein family classification
- **Domain Architecture**: Multi-domain protein analysis

## Files

| File | Description |
|------|-------------|
| `hmm_domain_analysis.ipynb` | Main analysis notebook |
| `data_analysis_and_processing.ipynb` | A small introduction to data analysis and processing |
| `output/` | Domain search results |

## Missing Data Files

| File | Description | Source |
|------|-------------|--------|
| `prots/*.faa` | ~100 protein FASTA files | UniProt batch download |
| `Pfam-A.hmm` | Pfam HMM database | [Pfam FTP](https://ftp.ebi.ac.uk/pub/databases/Pfam/) |

## Key Techniques

- HMM profile parsing and searching
- iE-value and coverage thresholds for filtering
- Domain co-occurrence analysis
