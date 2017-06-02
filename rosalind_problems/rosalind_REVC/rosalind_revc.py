from common_modules import read_file
from common_modules import complement_of_string

PROBLEM_FILE_PATH = 'D:/Bioinformaitcs Coding/rosalind_problems'

if __name__ == '__main__':
    dna_string = read_file(PROBLEM_FILE_PATH+'/rosalind_revc.txt')
    print(complement_of_string(dna_string[::-1]))
