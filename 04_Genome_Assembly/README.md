# Genome Assembly

De novo genome assembly using De Bruijn graph algorithms.

## Topics Covered

- **De Bruijn Graphs**: Graph-based representation of sequencing reads
- **K-mers**: Sequence fragmentation and overlap detection
- **Contig Assembly**: Building contiguous sequences from short reads

## Files

| File | Description |
|------|-------------|
| `de_bruijn_assembly.ipynb` | Main assembly notebook |
| `data/` | Input sequencing reads and outputs |

## Key Concepts

The De Bruijn graph approach:
1. Fragment reads into k-mers
2. Build a graph where nodes are (k-1)-mers
3. Edges represent k-mers connecting nodes
4. Find Eulerian paths to reconstruct sequences
