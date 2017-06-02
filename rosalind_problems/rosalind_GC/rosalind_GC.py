from common_modules import gc_count
from common_modules import read_fasta

PROBLEM_FILE_PATH = 'D:/Bioinformaitcs Coding/rosalind_problems'
OUTPUT_FILE_PATH = 'D:/Bioinformaitcs Coding/rosalind_answers'

# In this problem we would be given a fasta file containing 10 sequences with varying GC content
# We will utilize 2 modules from common_modules.py to read the fasta file and to compute the number
# of GC nucleotides in each sequence. Then we would measure GC% of each sequence and then
if __name__ == '__main__':
    # Reading the fasta file
    sequences = read_fasta(file_path=PROBLEM_FILE_PATH+'/rosalind_gc.txt')
    max_gc_key = ''
    max_gc_ratio = 0.0
    # Going through each sequence
    for key in sequences:
        gc_content = gc_count(sequences[key])
        sequence = sequences[key]
        gc_ratio = (gc_content/len(sequence))*100
        # If a sequence scores a higher gc_ratio than the current maximum score, then the
        # max_gc_ratio sequence is switched
        if gc_ratio > max_gc_ratio:
            max_gc_key = key
            max_gc_ratio = gc_ratio
    # Printing to the console
    print(max_gc_key)
    # We put an error of 0.0000001 to adhere to rosalind.info's standard error
    print('{0:.7f}'.format(max_gc_ratio))
    # Writing to an output file
    with open(OUTPUT_FILE_PATH+'/rosalind_gc_answer.txt', 'w') as write_file:
        write_file.write(max_gc_key)
        write_file.write('{0:.7f}'.format(max_gc_ratio))
