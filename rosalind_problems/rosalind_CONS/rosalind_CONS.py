from common_modules import read_fasta
from collections import defaultdict

PROBLEM_FILE_PATH = 'D:/Bioinformaitcs Coding/rosalind_problems'
nucleotide_sequence = ['A', 'C', 'G', 'T']

# The function takes in an iterator of some form containing all the sequences in string format
def get_consensus_profile(sequence_collection):
    # The consensus string. Empty at the start
    consensus_string = ''
    # This dictionary will contain 4 keys and lists for those 4 keys. The lists will contain the
    # number of bases (keys) at each location along the input strings
    nucleotide_sequence_dict = defaultdict(list)
    # First we use the zip function for easy iteration through all the bases, one location at
    # a time.
    for aligned in zip(*sequence_collection):
        # Using a defaultdict to count the number of bases at the specific location
        consensus_dict = defaultdict(int)
        for nucleotide in aligned:
            consensus_dict[nucleotide] += 1
        # Then using predefined nucleotide sequence (A, C, G, T), we add the number of occurences of each
        # base at the specific location.
        # A key error can arise since there's a possibility that a certain base was missing at this specific
        # location in all input strings. Therefore, when the error is raised we simply handle it by appending
        # '0' to the said location of the list for the relevant base
        for nucleotide in nucleotide_sequence:
            try:
                nucleotide_sequence_dict[nucleotide].append(consensus_dict[nucleotide])
            except KeyError:
                nucleotide_sequence_dict[nucleotide].append(0)
        # Now to form the consensus string, base by base
        # The consensus string is formed base by base. For each location we must find the base that occured the most
        # So we use 2 variables to accomplish this task
        max_number = 0
        max_nucleotide = ''
        # Then we loop through the consensus_dict for the specific location and find the base with the highest occurrence.
        for base in consensus_dict.keys():
            if consensus_dict[base] > max_number:
                max_nucleotide = base
                max_number = consensus_dict[base]
        # After the loop, we add the highest occurring nucleotide to the consensus string
        consensus_string += max_nucleotide
    # Finally we return the consensus string and the dictionary containing the number of occurrences for each nucleotide
    # at each location.
    return consensus_string, nucleotide_sequence_dict

if __name__ == '__main__':
    # Read the fasta file
    fasta_sequences = read_fasta(PROBLEM_FILE_PATH+'/rosalind_cons.txt')
    # Get out all the sequences, since the 'read_fasta' method returns results in form of dictionary
    sequence_list = [fasta_sequences[key] for key in fasta_sequences.keys()]
    # Get the consensus profile
    consensus_string, nucleotide_sequence_list = get_consensus_profile(sequence_list)
    # Print the consensus string
    print(consensus_string)
    # Then loop through the nucleotides and print out the number of occurrences for each nucleotide at
    # specific locations
    for base in nucleotide_sequence:
        print('{0}: {1}'.format(base, ' '.join([str(x) for x in nucleotide_sequence_list[base]])))
