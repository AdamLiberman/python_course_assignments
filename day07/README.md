'ncbi_downloader.py' takes a protein name as its first argument and search it against the protein database on NCBI. 
The second argument should be a number which represents the maximum nubmer of wanted matches to the protein name.
the code saves each result in a file of its own, on the output folder as "{name of protein searched}_{number of match}".
It also prints the names of all the saved files and adds the date of the search, the name of the searched protein, the number of maximum matches and the total number of results to a csv file named 'search.csv'.  