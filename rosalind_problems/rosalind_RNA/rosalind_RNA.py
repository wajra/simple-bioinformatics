from common_modules import read_file
from common_modules import dna_to_rna
import sys


PROBLEM_FILE_PATH = 'D:/Bioinformaitcs Coding/rosalind_problems'

if __name__ == '__main__':
    dna_string = read_file(PROBLEM_FILE_PATH+'/rosalind_rna.txt')
    print(dna_to_rna(dna_string))
