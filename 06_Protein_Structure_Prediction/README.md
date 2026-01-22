# Protein Structure Prediction

Comparative analysis of protein structure prediction methods.

## Topics Covered

- **I-TASSER**: Threading-based structure prediction
- **AlphaFold 2**: Deep learning structure prediction
- **AlphaFold 3**: Multi-molecular complex modeling

## Files

| File | Description |
|------|-------------|
| `INSTRUCTIONS.md` | Detailed exercise instructions |
| `data/` | Prediction results and experimental structures |

## Methods Compared

| Method | Approach | Key Metrics |
|--------|----------|-------------|
| I-TASSER | Threading + Monte Carlo | C-score, estimated TM-score |
| AlphaFold 2 | Evoformer + Structure Module | pLDDT, PAE |
| AlphaFold 3 | Diffusion models | Extended to DNA/RNA/ligands |

## Key Concepts

- Template-based vs. de novo prediction
- CASP competition targets
- Model quality assessment (TM-score, RMSD)
