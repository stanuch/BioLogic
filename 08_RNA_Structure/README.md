# RNA Structure Prediction

Implementation of the Nussinov algorithm for RNA secondary structure prediction.

## Topics Covered

- **Nussinov Algorithm**: Dynamic programming for base-pair maximization
- **Secondary Structure**: Dot-bracket notation and visualization
- **Bifurcation**: Handling of multi-branch loops

## Files

| File | Description |
|------|-------------|
| `img/` | Images of 2D structures used in `.ipynb` file|
| `nussinov.py` | Core algorithm implementation with loop constraints |
| `visualization.py` | Structures data visualization |
| `rna_structure_prediction.ipynb` | RNA structure prediction notebook |

## Algorithm Overview

The Nussinov algorithm uses dynamic programming to find the maximum number of base pairs:

```
For each subsequence (i,j):
  M[i,j] = max(
    M[i+1,j],           # i unpaired
    M[i,j-1],           # j unpaired
    M[i+1,j-1] + 1,     # i-j paired (if complementary)
    max(M[i,k] + M[k+1,j])  # bifurcation
  )
```

## Base Pairing Rules

| Pair | Type |
|------|------|
| A-U | Watson-Crick |
| G-C | Watson-Crick |
| G-U | Wobble (optional) |
