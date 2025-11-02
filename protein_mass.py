# 🧬 Python Mini Projects for Microbiology Applications
# Author: Memoona Razaq
# Objective: Apply Python concepts (data types, loops, functions, NumPy, etc.) to biological data problems.

# ==============================================================
# 1️⃣ PROTEIN MASS CALCULATION
# ==============================================================

# Dictionary of amino acid molecular weights (in Daltons)
amino_acid_weights = {
    'A': 89.09, 'R': 174.20, 'N': 132.12, 'D': 133.10, 'C': 121.15,
    'E': 147.13, 'Q': 146.15, 'G': 75.07, 'H': 155.16, 'I': 131.17,
    'L': 131.17, 'K': 146.19, 'M': 149.21, 'F': 165.19, 'P': 115.13,
    'S': 105.09, 'T': 119.12, 'W': 204.23, 'Y': 181.19, 'V': 117.15
}

def calculate_protein_mass(sequence):
    sequence = sequence.upper()
    total_mass = 0
    for aa in sequence:
        total_mass += amino_acid_weights.get(aa, 0)
    return round(total_mass, 2)

# Example usage:
protein_seq = "ACDEFGHIKLMNPQRSTVWY"
print("Protein sequence:", protein_seq)
print("Total protein mass:", calculate_protein_mass(protein_seq), "Daltons")

# ==============================================================
# 2️⃣ ENZYME REACTION SIMULATION (Michaelis–Menten Kinetics)
# ==============================================================

import numpy as np

def enzyme_rate(Vmax, Km, substrate_concentration):
    v = (Vmax * substrate_concentration) / (Km + substrate_concentration)
    return v

Vmax = 1.5   # Maximum reaction rate
Km = 0.5     # Michaelis constant

substrate_values = np.linspace(0.1, 5, 10)
reaction_rates = [enzyme_rate(Vmax, Km, s) for s in substrate_values]

print("\nSubstrate Concentration vs Reaction Rate:")
for s, v in zip(substrate_values, reaction_rates):
    print(f"[S]={s:.2f}  ->  v={v:.3f}")

# ==============================================================
# 3️⃣ DNA SEQUENCE ANALYSIS
# ==============================================================

def dna_analysis(dna_seq):
    dna_seq = dna_seq.upper()
    base_count = {base: dna_seq.count(base) for base in 'ATGC'}
    total_bases = sum(base_count.values())
    gc_content = ((base_count['G'] + base_count['C']) / total_bases) * 100
    richness = "GC-rich" if gc_content > 50 else "AT-rich"
    return base_count, round(gc_content, 2), richness

# Example usage
dna_seq = "ATGCGTACGTAGCTAGCTAGCTA"
counts, gc_percent, type_seq = dna_analysis(dna_seq)
print("\nDNA Base Counts:", counts)
print("GC Content:", gc_percent, "%")
print("Sequence Type:", type_seq)

# ==============================================================
# 4️⃣ CODON COUNTER
# ==============================================================

def codon_counter(dna_seq):
    dna_seq = dna_seq.upper()
    codons = [dna_seq[i:i+3] for i in range(0, len(dna_seq), 3) if len(dna_seq[i:i+3]) == 3]
    codon_freq = {codon: codons.count(codon) for codon in set(codons)}
    return codon_freq, len(codons)

# Example usage
dna_seq2 = "ATGCGTACTGATCGTACGTTGA"
frequency, total_codons = codon_counter(dna_seq2)
print("\nCodon Frequencies:", frequency)
print("Total Codons:", total_codons)
