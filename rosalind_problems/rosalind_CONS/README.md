# Consensus String  
A consensus string is a string that results from a collection of strings of equal length which has the most common character among the strings as it's own.  
This can be simply explained as below  
String #1 - **AATGCGAT**  
String #2 - **TATGCGTA**  
String #3 - **ATACGCAA**  
Consensus string - **AATGCGAA**

When going along the 3 strings simultaneously we see that a certain base is the one that occurs the most at a particular location.  
A string that is made up of all such bases in a collection of strings is the 'Consensus string'  
The code in rosalind_CONS.py file accomplishes this task by a function named 'get_consensus_profile'. The function takes in a single argument of a list 
of sequences and returns the consensus string and a dictionary object containing lists for the characters and their number in a specific location.
