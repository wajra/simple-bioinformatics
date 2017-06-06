from common_modules import read_file_multiple_sequences

PROBLEM_FILE_PATH = 'D:/Bioinformaitcs Coding/rosalind_problems'

# The function will have 2 inputs
# One would be the sequence and the other would be the short motif
# This function would return the indices of places in the sequence from which the motif can be found
def motif_match_locations(sequence, match_sequence):
    # Getting the length of the motif
    motif_length = len(match_sequence)
    print(motif_length)
    # The following list will hold the indices at which a motif starts in the sequence
    match_list = []
    for x in range(0, len(sequence)):
        # Starting from the beginning of the sequence we start to match
        # motifs of the specified length with the given motif
        if sequence[x:x+motif_length] == match_sequence:
            # If a match is made then it is added to 'match_list'
            # Since Python works in a zero-based indexing system, we have to add '1' for us to get the required values
            match_list.append(str(x+1))
    # Finally we join all the indices to a string and return it
    return ' '.join(match_list)


if __name__ == '__main__':
    sequence, motif = read_file_multiple_sequences(PROBLEM_FILE_PATH+'/rosalind_subs.txt')
    print(motif_match_locations(sequence, motif))
