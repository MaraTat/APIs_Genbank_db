# APIs for data extraction from an SQL database

The code included here is my own work from a coursework during my Bioinformatics studies 

The APIs are tailored to the database created from repo Create_Populate_Database_mySQL so please look there first to understand the variable names

The best feature of these APIs is that you can use any query item e.g. gene name or protein name etc and you'll get the information you need

## Look out for

The output of the functions is a string but you can easily change that to a tuple or whatever suits your needs

The data to be inserted can be imported as a module at the top or as single files from your computer. Configuration information for the database is external and needs to be imported at the top as well for your own db

## APIs for:

| Function | Details |
|-------------|-------|
|getDNA|DNA sequence|
|getprot|protein sequence|
|getgenesize|full gene size|
|getCDS|all CDS join points|
|getCDS_properties|CDS strand complement or not|
|getAccession|entry accession number|
|getLocation|entry chromosomal location|


### Additional APIs for:

| Function | Details |
|-------------|-------|
|getGeneName|gene name when queried with protein name or chromosomal location|
|getProtName|protein name when queried with gene name or chromosomal location|



As always help yourselves and help others if you can :-) 


If you have any issues don't hesitate to drop me a line, always happy to help!!
