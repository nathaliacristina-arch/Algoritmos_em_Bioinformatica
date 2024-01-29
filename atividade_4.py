# -*- coding: utf-8 -*-
"""Atividade_4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1foKhW-DXEF9y4dV9fe688IIXejm9gn_x
"""

# Identificar regiões do genoma da H3N2 que potencialmente codificam proteínas. Analisar e identificar em cada segmento e em cada frame da sequência traduzida do genoma da H3N2 e gravar num único arquivo fasta.

# Enviar:

# 1- Código

# 2 - Um único arquivo fasta com todos as potenciais sequências que codificam proteínas identificando o segmento, frame e o número da sequência dentro do segmento.

# Ex. de arquivo fasta do inte 2:

# >H3N2, Frame 1, segmento 1, proteína 1

# MSDHEGG.............................................................*

# >H3N2, Frame 1, segmento 1, proteína 2

# MYGDHSJKK..............*

# >H3N2, Frame 1, segmento 1, proteína 3

# MVFFSSS.............*

# .
# .
# >H3N2, Frame 3, segmento 7, proteína 7

# MGHHHHDGDBGYYYYYDTDYY...............................................*

# .
# .
# .
# >H3N2, Frame 6, segmento 8, proteína 13

# MHDYSGDTEBFHUSGDHSUUD...............................

# .........................................................................................*

# MYGDHSJKK..............*

!pip install biopython
from Bio import SeqIO
from Bio.Seq import Seq
#from Bio.Alphabet import IUPAC
from Bio.SeqUtils import six_frame_translations

# Abrir o arquivo fasta contendo a sequência do genoma da Influenza H3N2
file_path = "Influenza H3N2 (1) (1).fasta"
for record in SeqIO.parse(file_path, "fasta"):
    sequence = str(record.seq)

# lê o arquivo FASTA
records = SeqIO.parse(file_path, "fasta")

# cria um dicionário para armazenar as traduções
translations = {}

# percorre os registros
for record in records:
    # obtém a sequência do registro como uma string
    sequence = str(record.seq)

    # cria um objeto Seq a partir da sequência de DNA
    dna_seq = Seq(sequence)

    # cria uma lista com todas as possíveis traduções
    for strand, nuc in [(+1, dna_seq), (-1, dna_seq.reverse_complement())]:
        for frame in range(3):
            translation = str(nuc[frame:].translate())
            translations[(strand, frame)] = translation

# escreve as regiões codificadoras em um arquivo FASTA
with open(file_path, "w") as output_file:
    seq_num = 1
    for segment in range(1, 9):
        for frame in range(3):
            protein_num = 1
            for translation in translations[(+1, frame)].split("*"):
                if len(translation) >= 30:
                    output_file.write(f">H3N2, Frame {frame + 1}, segmento {segment}, proteína {protein_num}\n")
                    output_file.write(f"{translation}*\n")
                    protein_num += 1
                seq_num += 1