from common_modules import read_file
from common_modules import count_nucleotides

PROBLEM_FILE_PATH = 'D:/Bioinformaitcs Coding/rosalind_problems'

if __name__ == '__main__':
    dna_string = read_file(PROBLEM_FILE_PATH+'/rosalind_dna.txt')
    key_order = ['A', 'C', 'G', 'T']
    counter_result = count_nucleotides(dna_string)
    print(' '.join([str(counter_result[nucleotide]) for nucleotide in key_order]))
