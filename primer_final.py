def complementaridade(seq1, seq2=None):
    # Definindo o dicionário de bases complementares
    complementar = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # Se seq2 não for fornecida, utilizamos seq1 para calcular a complementaridade com ela mesma
    if seq2 is None:
        seq2 = seq1
    
    # Gerando a sequência complementar reversa de seq2
    seq_complementar = "".join(complementar[base] for base in reversed(seq2))
    
    # Contando o número de pares complementares entre seq1 e a seq_complementar
    complementar_count = sum(1 for a, b in zip(seq1, seq_complementar) if a == b)
    
    # Calculando a porcentagem de complementaridade
    complementaridade_percentual = (complementar_count / len(seq1)) * 100
    
    return complementaridade_percentual

def calcular_percentual_bases(seq):
    total_bases = len(seq)
    a_t_count = seq.count('A') + seq.count('T')
    g_c_count = seq.count('G') + seq.count('C')
    
    percentual_at = (a_t_count / total_bases) * 100
    percentual_gc = (g_c_count / total_bases) * 100
    
    return percentual_at, percentual_gc

# Inputs
primer_foward = input("Insira o primer forward: ").upper()
primer_reverse = input("Insira o primer reverse: ").upper()

# Complementaridade do primer forward com ele mesmo
resultado_foward = complementaridade(primer_foward)
print(f"O primer forward é {resultado_foward:.2f}% complementar a ele mesmo.")

# Cálculo das porcentagens de A/T e G/C no primer forward
percentual_at_foward, percentual_gc_foward = calcular_percentual_bases(primer_foward)
print(f"O primer forward tem {percentual_at_foward:.2f}% de A/T e {percentual_gc_foward:.2f}% de G/C.")

# Complementaridade do primer reverse com ele mesmo
resultado_reverse = complementaridade(primer_reverse)
print(f"O primer reverse é {resultado_reverse:.2f}% complementar a ele mesmo.")

# Cálculo das porcentagens de A/T e G/C no primer reverse
percentual_at_reverse, percentual_gc_reverse = calcular_percentual_bases(primer_reverse)
print(f"O primer reverse tem {percentual_at_reverse:.2f}% de A/T e {percentual_gc_reverse:.2f}% de G/C.")

# Complementaridade entre o primer forward e o primer reverse
resultado_entre = complementaridade(primer_foward, primer_reverse)
print(f"O primer forward é {resultado_entre:.2f}% complementar ao primer reverse.")

