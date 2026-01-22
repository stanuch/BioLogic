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
| `img/` | Output visualizations |

## Missing Data Files

| File | Size | Description |
|------|------|-------------|
| `*.map` | ~5 MB each | CCP4 format electron density maps |

Maps can be downloaded from the [PDB Electron Density Server](https://www.ebi.ac.uk/pdbe/eds/).

## Key Concepts

- Map coefficients (2Fo-Fc, Fo-Fc)
- Contour levels (typically 1σ, 3σ)
- Radiation damage indicators
