# -*- coding: utf-8 -*-
"""Atividade_9

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jidKw72JOavgUK3I47njRKXELJptnN_z
"""

# Alinhamento local
# - Local:
# o alinhamento localiza fragmentos de sequências que são mais similares.
# ALGORITMO DE SMITH-WATERMAN - alinhamento local. Utiliza - Programação dinâmica:
# - Método computacional que calcula o melhor alinhamento possível entre sequências. Principais variáveis do programa:
# match = +5
# mismatch = -3
# gap = -4

# Figura 1: Inicializacao da Matriz

# Variaveis:
#           i,j - linhas e colunas.
#           M - matriz de valores
#           S - o escore da celula requerida (Si, j)
#           W - gap

# Para preencher cada celula da matriz de Programação dinâmica





# Figure 2: Matrix preenchida e os back pointers.


# Resultado esperado (submeter):

# A) Descreva com detalhes como a programação dinâmica é utilizada para fazer o alinhamento de sequência. (Dissertativa)

# B) O código do program de alinhamento local (Programação dinâmica)

# C) A matriz de escore do alinhamento local (Programação dinâmica)

# E) O alinhamento e o escore total das duas sequencias como a Fig. 5 do link abaixo.
# http://vlab.amrita.edu/?sub=3&brch=274&sim=1433&cnt=1

# Figure 5: Scoring for best alignment

# F) Teste o Alinhamento de duas sequências abaixo:
# seq1: GAATTCAGTTA
# seq2: GGATCGA

def smith_waterman(seq1, seq2, match, mismatch, gap):
    m = len(seq1)
    n = len(seq2)

    # Inicialização da matriz com zeros
    score_matrix = [[0] * (n + 1) for _ in range(m + 1)]

    # Preenchimento da matriz
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Cálculo dos valores para a célula (i, j)
            diagonal_score = score_matrix[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch)
            up_score = score_matrix[i - 1][j] + gap
            left_score = score_matrix[i][j - 1] + gap

            # Atualização do valor da célula (i, j)
            score_matrix[i][j] = max(0, diagonal_score, up_score, left_score)

    return score_matrix

# Exemplo de uso
seq1 = "GAATTCAGTTA"
seq2 = "GGATCGA"
match = 5
mismatch = -3
gap = -4

score_matrix = smith_waterman(seq1, seq2, match, mismatch, gap)

# Recuperação do alinhamento ótimo
def retrieve_alignment(seq1, seq2, score_matrix):
    m = len(seq1)
    n = len(seq2)
    max_score = 0
    max_i = 0
    max_j = 0

    # Encontrar a célula com o maior escore na matriz
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if score_matrix[i][j] > max_score:
                max_score = score_matrix[i][j]
                max_i = i
                max_j = j

    # Reconstruir o alinhamento ótimo a partir da célula com o maior escore
    alignment_seq1 = ""
    alignment_seq2 = ""
    score = max_score

    while score > 0 and max_i > 0 and max_j > 0:
        if score_matrix[max_i][max_j] == score_matrix[max_i - 1][max_j - 1] + (match if seq1[max_i - 1] == seq2[max_j - 1] else mismatch):
            alignment_seq1 = seq1[max_i - 1] + alignment_seq1
            alignment_seq2 = seq2[max_j - 1] + alignment_seq2
            score -= match if seq1[max_i - 1] == seq2[max_j - 1] else mismatch
            max_i -= 1
            max_j -= 1
        elif score_matrix[max_i][max_j] == score_matrix[max_i - 1][max_j] + gap:
            alignment_seq1 = seq1[max_i - 1] + alignment_seq1
            alignment_seq2 = "-" + alignment_seq2
            score -= gap
            max_i -= 1
        else:
            alignment_seq1 = "-" + alignment_seq1
            alignment_seq2 = seq2[max_j - 1] + alignment_seq2
            score -= gap
            max_j -= 1

    return alignment_seq1, alignment_seq2, max_score

# Executando o teste novamente
alignment_seq1, alignment_seq2, alignment_score = retrieve_alignment(seq1, seq2, score_matrix)

print("Alinhamento:")
print(alignment_seq1)
print(alignment_seq2)
print("Escore total:", alignment_score)

def smith_waterman(seq1, seq2, match, mismatch, gap):
    m = len(seq1)
    n = len(seq2)

    # Inicialização da matriz com zeros
    score_matrix = [[0] * (n + 1) for _ in range(m + 1)]

    # Preenchimento da matriz
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Cálculo dos valores para a célula (i, j)
            diagonal_score = score_matrix[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch)
            up_score = score_matrix[i - 1][j] + gap
            left_score = score_matrix[i][j - 1] + gap

            # Atualização do valor da célula (i, j)
            score_matrix[i][j] = max(0, diagonal_score, up_score, left_score)

    # Recuperação do alinhamento ótimo
    def retrieve_alignment():
        max_score = 0
        max_i = 0
        max_j = 0

        # Encontrar a célula com o maior escore na matriz
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if score_matrix[i][j] > max_score:
                    max_score = score_matrix[i][j]
                    max_i = i
                    max_j = j

        # Reconstruir o alinhamento ótimo a partir da célula com o maior escore
        alignment_seq1 = ""
        alignment_seq2 = ""
        score = max_score

        while score > 0 and max_i > 0 and max_j > 0:
            if score_matrix[max_i][max_j] == score_matrix[max_i - 1][max_j - 1] + (match if seq1[max_i - 1] == seq2[max_j - 1] else mismatch):
                alignment_seq1 = seq1[max_i - 1] + alignment_seq1
                alignment_seq2 = seq2[max_j - 1] + alignment_seq2
                score -= match if seq1[max_i - 1] == seq2[max_j - 1] else mismatch
                max_i -= 1
                max_j -= 1
            elif score_matrix[max_i][max_j] == score_matrix[max_i - 1][max_j] + gap:
                alignment_seq1 = seq1[max_i - 1] + alignment_seq1
                alignment_seq2 = "-" + alignment_seq2
                score -= gap
                max_i -= 1
            else:
                alignment_seq1 = "-" + alignment_seq1
                alignment_seq2 = seq2[max_j - 1] + alignment_seq2
                score -= gap
                max_j -= 1

        return alignment_seq1, alignment_seq2, max_score

    alignment_seq1, alignment_seq2, alignment_score = retrieve_alignment()

    return alignment_seq1, alignment_seq2, alignment_score, score_matrix

# Exemplo de uso
seq1 = "GAATTCAGTTA"
seq2 = "GGATCGA"
match = 5
mismatch = -3
gap = -4

alignment_seq1, alignment_seq2, alignment_score, score_matrix = smith_waterman(seq1, seq2, match, mismatch, gap)

# Exibição da matriz de escore
print("Matriz de Escore:")
for row in score_matrix:
    print(row)

# Exibição do alinhamento e do escore total
print("\nAlinhamento:")
print(alignment_seq1)
print(alignment_seq2)
print("Escore total:", alignment_score)