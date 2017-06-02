from common_modules import read_file_multiple_sequences
from common_modules import hamming_distance

PROBLEM_FILE_PATH = 'D:/Bioinformaitcs Coding/rosalind_problems'

if __name__ == '__main__':
    string_1, string_2 = read_file_multiple_sequences(PROBLEM_FILE_PATH+'/rosalind_hamm.txt')
    print(hamming_distance(string_1, string_2))
