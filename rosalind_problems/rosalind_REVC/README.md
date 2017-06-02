# Reverse complementing a DNA sequence  
The reverse complement of a DNA string would mean to  
1. Reverse a DNA string  
AATGGGCGAAT -> TAAGCGGGTAA  
2. And then complement that sequence (A <-> T, G <-> C)  
ATTCGCCCATT  
We accomplish this task by reverse slicing the DNA sequence using [::-1] and then using a small function in the 'common_modules.py' module to complement the reverseed sequence
