import numpy as np
import matplotlib.pyplot as plt

energies = [
    -28.10, -27.90, -27.80, -27.80, -27.60, -27.50,
    -27.20, -27.20, -27.20, -27.20, -27.10, -27.00,
    -27.00, -27.00, -27.00, -27.00, -27.00, -26.70,
    -26.70, -26.70, -26.70, -26.70
]

R = 0.001985875 
T = 273 + 37 
RT = R * T

boltzmann_factors = [np.exp(-e / RT) for e in energies]
Z = sum(boltzmann_factors)

print(f"Suma statystyczna Z: {Z:.4e}")
print("-" * 50)
print(f"{'Energia (kcal/mol)':<20} | {'Prawdopodobieństwo':<20}")
print("-" * 50)

probs_individual = [bf / Z for bf in boltzmann_factors]

unique_energies = sorted(list(set(energies)))
probs_summed = []

for u_e in unique_energies:
    count = energies.count(u_e)
    p_single = np.exp(-u_e / RT) / Z
    p_total = count * p_single
    probs_summed.append(p_total)
    
    print(f"{u_e:<20.2f} | {p_total:.4f}")

probs_unique_single = [np.exp(-e / RT) / Z for e in unique_energies]

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(unique_energies, probs_unique_single, 'bo-', label='Pojedyncza struktura')
plt.title("Prawdopodobieństwo pojedynczej struktury")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.bar(unique_energies, probs_summed, width=0.1, color='green', label='Suma prawdopodobieństw')
plt.title("Sumaryczne prawdopodobieństwo dla energii")
plt.grid(axis='y')

plt.tight_layout()
plt.show()