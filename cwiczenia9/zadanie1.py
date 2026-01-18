import numpy as np
import os

def parse_pdb_file(file_path):
    atom_data = []

    # TODO:
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                
                atom_name = line[12:16].strip()
                res_seq = int(line[22:26].strip())
                chain_id = line[21].strip()
                
                atom_info = {
                    'x': x, 'y': y, 'z': z,
                    'name': atom_name,
                    'resid': res_seq,
                    'chain': chain_id
                }
                atom_data.append(atom_info)
    return atom_data

# użycie funkcji
reference_pdb_path = './data/7qvb_A.pdb'
model_pdb_path     = './data/af2_pred.pdb'

reference_data = parse_pdb_file(reference_pdb_path)
model_data     = parse_pdb_file(model_pdb_path)

def filter_atom_data(atom_data, residue_numbers, atom_name):
    filtered_atom_data = []

    # TODO:
    filtered_atom_data = []
    residue_set = set(residue_numbers)

    for atom in atom_data:
        if atom['resid'] in residue_set and atom['name'] == atom_name:
            filtered_atom_data.append(atom)

    return filtered_atom_data

# użycie funkcji
atom_name_to_filter = 'CA'

filtered_reference_data = filter_atom_data(
    reference_data,
    list(range(5,159)),
    atom_name_to_filter
)

filtered_model_data = filter_atom_data(
    model_data,
    list(range(9,163)),
    atom_name_to_filter
)

def extract_xyz_positions(atom_data):
    # TODO:
    coords = [[atom['x'], atom['y'], atom['z']] for atom in atom_data]
    return np.array(coords)

# użycie funkcji
filtered_reference_data_xyz = extract_xyz_positions(filtered_reference_data)
filtered_model_data_xyz     = extract_xyz_positions(filtered_model_data)

def align_coordinates(xyz_moving_A, xyz_fixed_B):
    # TODO:
    centroid_A = np.mean(xyz_moving_A, axis=0)
    centroid_B = np.mean(xyz_fixed_B, axis=0)

    A_centered = xyz_moving_A - centroid_A
    B_centered = xyz_fixed_B - centroid_B

    H = A_centered.T @ B_centered
    U, S, Vt = np.linalg.svd(H)

    R = Vt.T @ U.T
    t = centroid_B - (centroid_A @ R.T)

    return R, t

# użycie funkcji
R, t = align_coordinates(
    filtered_model_data_xyz,
    filtered_reference_data_xyz
)

filtered_model_data_xyz_fitted = filtered_model_data_xyz @ R.T + t

def calculate_rmsd(xyz_A, xyz_B):
    # TODO:       
    N = xyz_A.shape[0]
    diff = xyz_A - xyz_B
    sq_diff = np.sum(diff**2)
    rmsd = np.sqrt(sq_diff / N)

    return rmsd

print(
    f"RMSD pre fit:  {calculate_rmsd(filtered_reference_data_xyz, filtered_model_data_xyz):.3f} Å"
)
print(
    f"RMSD post fit: {calculate_rmsd(filtered_reference_data_xyz, filtered_model_data_xyz_fitted):.3f} Å"
)