AMINO_ACID_MASSES = [
    57, 71, 87, 97, 99, 101, 103, 113, 114,
    115, 128, 129, 131, 137, 147, 156, 163, 186
]

def count_peptides_with_mass(target_mass):
    dp = [0] * (target_mass + 1)
    dp[0] = 1  # one way to make mass 0 (empty peptide)

    for mass in range(1, target_mass + 1):
        for a in AMINO_ACID_MASSES:
            if mass - a >= 0:
                dp[mass] += dp[mass - a]
    return dp[target_mass]

# Example usage:
print(count_peptides_with_mass(1332))