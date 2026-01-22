# Single-Cell RNA Sequencing

Introduction to single-cell transcriptomics analysis in R.

## Topics Covered

- **scRNA-seq Workflow**: From counts matrix to cell types
- **Dimensionality Reduction**: PCA and clustering
- **Differential Expression**: Identifying marker genes

## Files

| File | Description |
|------|-------------|
| `scrna_introduction.Rmd` | R Markdown analysis document |
| `data/Samples.csv` | Sample metadata |

## Missing Data Files

| File | Size | Description |
|------|------|-------------|
| `data/Cells.csv` | ~2.4 MB | Cell expression matrix |
| `data/Genes.txt` | ~175 KB | Gene annotations |
| `data/Exp_data_UMIcounts.mtx` | ~780.7 MB | Expression data |

These files were provided as course materials.

## Prerequisites

```r
# R packages required
install.packages(c("Seurat", "dplyr", "ggplot2"))
```
