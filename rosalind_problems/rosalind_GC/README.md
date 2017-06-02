# Calculating the GC content of a sequence and ranking several sequences in terms of GC content  

Then problem presents us with at least 10 different sequences in fasta file format. The objective is to compute the GC content of 
each sequence and then output the fasta id of the sequence with the highest GC% along with the GC%.  
We utilize 2 modules in common_modules.py to accomplish most of the task including reading the fasta file into a dictionary and then
calculating the number of GC nucleotides in the sequence.
