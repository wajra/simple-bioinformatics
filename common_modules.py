import random
import os.path

# Generates a random DNA string of default length 1000 (Can be of any specified length)
def generate_random_string(length=1000):
    return ''.join([random.choice('GCAT') for _ in range(length)])

# Hamming distance is the number of mismatches among 2 sequences
# GCGTAAATCGG
#   | |||
# GCTTGCCTCGG
# Among those 2 strings, hamming distance is 4
def hamming_distance(string_1, string_2):
    return len([x for x, y in zip(string_1, string_2) if x != y])

# Reads .fasta files and returns sequences as follows
# >seq01
# AAATGACGGTTTCC
# Will be returned in the shape of a dictionary
# 'seq01':'AAATGACGGTTTCC' with 'seq01' as the key and sequence as item
# This function would return a FileNotFoundError in case of an incorrect path
def read_fasta(file_path):
    string_dict = dict()
    # First we check if the file path exists
    if os.path.exists(file_path):
        with open(file_path, 'r') as fasta_file:
            string_id = ''
            for line in fasta_file:
                if line.startswith('>'):
                    print('Yes')
                    string_id = line[1:]
                    string_dict[string_id] = ''
                else:
                    string_dict[string_id] += line.strip()
    else:
        return FileNotFoundError('File was not found.')
    return string_dict

# Counts the number of times 'G' and 'C' bases are found on a string
def gc_count(string_1):
    return string_1.count('G')+string_1.count('C')

# Reads a simple text file and appends all the sequences to a single string and returns
def read_file(file_path):
    return_string = ''
    if os.path.exists(file_path):
        with open(file_path, 'r') as string_file:
            for line in string_file:
                return_string+=line.strip()
    else:
        return FileNotFoundError('File was not found')
    return return_string

# Translates a DNA sequence to RNA sequence.
# 'T' -> 'U'
def dna_to_rna(string_1):
    return string_1.replace('T', 'U')

# Does the opposite of the previous method
# 'U' -> 'T'
def rna_to_dna(string_1):
    return string_1.replace('U', 'T')

# Complementary bases are the bases which can form H-bonds
# For 'A' that is 'T'
# For 'G' that is 'C'
def complement_of_string(string_1):
    complement_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    complement_string = ''.join([complement_dict[base] for base in string_1])
    return complement_string

# Testing the available functions
if __name__ == '__main__':
    # Generating a random string and printing it
    print(generate_random_string(length=10))

    # Finding out the hamming distance (number of difference base pairs) between 2 genes
    random_string_1 = generate_random_string(length=20)
    random_string_2 = generate_random_string(length=20)
    print(random_string_1)
    print(random_string_2)
    print(hamming_distance(random_string_1, random_string_1))


    # Reading a fasta file
    fasta_dict = read_fasta(file_path='D:/Bioinformaitcs Coding/Samples/sequence.fasta')
    for key in fasta_dict:
        print(key)
        print(fasta_dict[key])
        print(len(fasta_dict[key]))
        print(gc_count(fasta_dict[key]))

    # Getting the complement of a string
    string = rna_to_dna('GGUACCAUCCUCUACUGUCGCCAGACUACAUUAGUCAACACCCGUCCGCCGCAUUGCAUUAAUGCCUUCUAAUGAUGGUGCCAACGACUUUGAUGCGAGUUCCAGGGGAGUCACGCACACUAACCUCCAGAUGCCAACGAUUCGGGUGAUCCCAUCCUCCCCACCGGUUCGGAUGCAAGCGGUGUUCGAGCACGAGCGCAGGCCCUACCGAGAGUAGAUAGCAAUCCUAAUUGUCGCAAGCGAUGACGGUAUGAGUUAGGAUCGCACCGCCAAAACCCAAAAUGCCGCGUGCAAUUCCGGGCUGACGGAAUUCCUCGAACUUCGAACCCGGCCUCUACGGCCCGUUAGCUGAUUGAUCGCCCUGUGAACUGGCAGUGGUCAGGGUCUGUCCGAGCGUUGAGAUGUAAGUGUACGGUGAGUAGCAGAGGCUUAAGUCAGGCAAUACUACCCGCGUUUAUUGUAGGUGUAGUACUGGUCCAUAGACAAUCACGAUACUCAGAGGCGAGAUCCUUAGCUGCGGCUCCUAUUGGUUUCUCCCGUUAGGUCUGAUAGUAGUCUACCAUGGAGUGUGGAUACACGUCAUGUCAAGGGACCCGUCUAAUAGGGAUAACAUCAGUAUCUACACGUAACUGGUCACGCUCAUAGACAGCCCGGCUAGCUUCUGUGGUCCAUAAAGCUUGGAUGAGGUACUAUUUGGUACAUAGAUCACCUAUGAGUCGUCAUGCGAAUCGCGGAAGUGGAUAAAAUCGCGAAAUUCUCACGGUCUUAUCCUUACCGGCCAUCGUUUGACCCCGGGAUUGUGUUAGGGAAUGGGCCUAACGUCUCAUUUCUCGUCUUACCAUUGGGGUGAAUUCCACUUGCAAAAACGAAACACGACACUUUUGAUUAGCGAUCUUUAAAUUUAACAUGCUUUCAUCGUCAUACAACCGUUGAACGCCACAAGCUAAGGCCCGUGUUCCGGGAUAGUUGCUGAGCAAG')
    print(complement_of_string(string[:100]))
