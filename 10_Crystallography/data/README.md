# Crystallography

Electron density map analysis and radiation damage assessment.

## Topics Covered

- **Electron Density Maps**: 2Fo-Fc and Fo-Fc map interpretation
- **Radiation Damage**: Effects of X-ray exposure on protein crystals
- **PyMOL Visualization**: Map rendering and analysis

## Files

| File | Description |
|------|-------------|
| `electron_density_analysis.ipynb` | Main analysis notebook |
| `damage_scenes.py` | PyMOL scene generation |
| `notes.txt` | Personal notes and observations |
| `data/` | Input data files |
| `img/` | Output visualizations |

## Excluded Data Files

Large data files are excluded from the repository via `.gitignore`:

| File | Description |
|------|-------------|
| `*.map` | CCP4 format electron density maps |
| `*.cif` | mmCIF structure files |

These can be downloaded from:
- [PDB Electron Density Server](https://www.ebi.ac.uk/pdbe/eds/) (maps)
- [RCSB PDB](https://www.rcsb.org/) (CIF files, e.g. 3T96, 4MS4)

## Key Concepts

- Map coefficients (2Fo-Fc, Fo-Fc)
- Contour levels (typically 1σ, 3σ)
- Radiation damage indicators
