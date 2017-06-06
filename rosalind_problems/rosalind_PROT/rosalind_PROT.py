import csv
import os.path
from common_modules import read_file

PROBLEM_FILE_PATH = 'D:/Bioinformaitcs Coding/rosalind_problems'

def get_codon_dict(file='D:/Bioinformaitcs Coding/rosalind_problems/codon_to_protein.csv'):
    if os.path.exists(file):
        codon_dict = dict()
        with open(file, 'r') as codon_file:
            csv_reader = csv.DictReader(codon_file)
            for line in csv_reader:
                codon_dict[line['codon']] = line['amino_acid']
        return codon_dict
    else:
        return None

def rna_to_protein(sequence):
    codon_dict = get_codon_dict()
    protein = ''
    for x in range(0, len(sequence), 3):
        amino_acid = codon_dict[sequence[x:x+3]]
        if amino_acid == 'Stop':
            break
        else:
            protein += amino_acid
    # return ''.join([codon_dict[sequence[x:x+3]] for x in range(0, len(sequence), 3)])
    return protein

if __name__ == '__main__':
    rna_sequence = read_file(PROBLEM_FILE_PATH+'/rosalind_prot.txt')
    print(rna_to_protein(rna_sequence))

