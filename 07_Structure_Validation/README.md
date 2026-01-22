# Structure Validation

Mathematical validation of protein structural models.

## Topics Covered

- **Kabsch Algorithm**: Optimal superposition using SVD
- **RMSD Calculation**: Root-mean-square deviation of atomic coordinates
- **TM-score & GDT_TS**: Global and local quality metrics

## Files

| File | Description |
|------|-------------|
| `kabsch_rmsd.ipynb` | Implementation of structural alignment |
| `INSTRUCTIONS.md` | Detailed exercise instructions |
| `data/` | PDB structures for validation |

## Mathematical Background

The Kabsch algorithm finds the optimal rotation matrix R to minimize RMSD:

1. Center both structures at origin
2. Compute covariance matrix H = AᵀB
3. Apply SVD: H = UΣVᵀ
4. Calculate rotation: R = VUᵀ
5. Handle reflection case if det(R) < 0

## Key Metrics

| Metric | Range | Interpretation |
|--------|-------|----------------|
| RMSD | 0 - ∞ Å | Lower is better, <2Å is good |
| TM-score | 0 - 1 | >0.5 indicates same fold |
| GDT_TS | 0 - 100% | Higher is better |
