#!/usr/bin/env python3

#==============================================================================
# Importing necessary libraries

import pymysql
import pymysql.cursors

# don't forget to import your connection_config_dict with the connection details

#==============================================================================
# Set of APIs to extract DNA sequence, protein sequence, CDS information (e.g. complement)
# CDS joins, gene and protein names and chromosomal location from the genbank database

# The best feature of these APIs is that you can use any query item and you'll get the information you need
# The APIs are tailored to the database created from repo Create_Populate_Database_mySQL so please look there first

def getDNA(arg):
    """ This function accepts a single argument which can be the accession number 
        or the name of a gene or the chromosomal location or the protein name
        and returns the complete sequence of that gene exon/intron including
        
        Input = accesion or gene_id or chromosomal location or protein name
        Return = string with the complete gene sequence
    """
        
    connection = pymysql.connect(**connection_config_dict)
    cursor = connection.cursor()
    query = "SELECT dna_seq FROM yourtable WHERE accession =%s OR gene_name=%s OR location=%s OR protein_name=%s"
    cursor.execute(query, (arg,arg,arg, arg))
    row = cursor.fetchone()

    if row: 
        DNA = str(row[0].strip())
    else:
        DNA = None
    connection.close()
    return DNA

#==============================================================================

def getprot(arg):
    """ This function accepts a single argument which can be the accession number 
        or the name of a gene or the chromosomal location or the protein name
        and returns the protein sequence this gene encodes for
        
        Input = accesion or gene_id or chromosomal location or protein name
        Return = string with the protein sequence or None if empty
    """
    
    connection = pymysql.connect(**connection_config_dict)
    cursor = connection.cursor()
    query = "SELECT protein_seq FROM yourtable WHERE accession =%s OR gene_name=%s OR location=%s OR protein_name=%s"
    cursor.execute(query, (arg,arg, arg, arg))
    row = cursor.fetchone()
    
    if row: 
        protein = str(row[0].strip())
    else:
        protein = None
    connection.close()
    return protein

#==============================================================================

def getgenesize(arg):
    """ This function accepts a single argument which can be the accession number 
        or the name of a gene or the chromosomal location or the protein name
        and returns the total size of the gene in bp
        
        Input = accesion or gene_id or chromosomal location or protein name
        Return = integer of the full gene size or None if empty
    """
    
    connection = pymysql.connect(**connection_config_dict)
    cursor = connection.cursor()
    query = "SELECT gene_size FROM yourtable WHERE accession =%s OR gene_name=%s OR location=%s OR protein_name=%s"
    cursor.execute(query, (arg,arg,arg,arg))
    row = cursor.fetchone()
    
    if row: 
        genesize = row[0]
    else:
        genesize = None
    connection.close()
    return genesize

#==============================================================================

def getCDS(arg):
    """ This function accepts a single argument which can be the accession number 
        or the name of a gene or the chromosomal location or the protein name
        and returns all the joining points that form the final coding sequence 
        of a gene this is to be used for intron/exon markings by the BL
        
        Input = accesion or gene_id or chromosomal location or protein name
        Return = tuple including all the CDS join points of the gene or None if empty
    """
    connection = pymysql.connect(**connection_config_dict)
    cursor = connection.cursor()
    query = "SELECT cds_joins FROM yourtable WHERE accession =%s OR gene_name=%s OR location=%s OR protein_name=%s"
    cursor.execute(query, (arg,arg,arg,arg))
    row = cursor.fetchone()
      
    if row: 
        CDS_full = row[0]     
    else:
        CDS_full = None
    connection.close()
    return CDS_full

#==============================================================================

def getCDS_properties(arg):
    """ This function accepts a single argument which can be the accession number 
        or the name of a gene or the chromosomal location or the protein name
        and returns the information that accompanies the CDS in the genbank file
        which indicates whether the CDS is in the complement strand or not
             
        Input = accesion or gene_id or chromosomal location or protein name
        Return = string which states 'complement' or None if empty
    """
    
    connection = pymysql.connect(**connection_config_dict)
    cursor = connection.cursor()
    query = "SELECT cds_info FROM yourtable WHERE accession =%s OR gene_name=%s OR location=%s OR protein_name=%s"
    cursor.execute(query, (arg,arg,arg,arg))
    row = cursor.fetchone()
      
    if row: 
        CDS_comment = row[0]     
    else:
        CDS_comment = None
    connection.close()
    return CDS_comment
    
#==============================================================================

def getAccession(arg):
    """ This function accepts a single argument which can be the name of a gene 
        or the chromosomal location or the protein name and returns the accession number 
                     
        Input = gene_id or chromosomal location or protein name
        Return = string with the accession number or None if empty
    """
    
    connection = pymysql.connect(**connection_config_dict)
    cursor = connection.cursor()
    query = "SELECT accession FROM yourtable WHERE gene_name=%s OR location=%s OR protein_name=%s"
    cursor.execute(query, (arg,arg,arg))
    row = cursor.fetchone()
      
    if row: 
        accession = row[0]     
    else:
        accession = None
    connection.close()
    return accession

#==============================================================================

def getLocation(arg):
    """ This function accepts a single argument which can be the accession number 
        or the name of a gene or the protein name and returns the entry location where available 
             
        Input = accesion or gene_id or chromosomal location or protein name
        Return = string with the location information or None if empty
    """
    
    connection = pymysql.connect(**connection_config_dict)
    cursor = connection.cursor()
    query = "SELECT location FROM yourtable WHERE accession =%s OR gene_name=%s OR protein_name=%s"
    cursor.execute(query, (arg,arg,arg))
    row = cursor.fetchone()
      
    if row: 
        location = row[0]     
    else:
        location = None
    connection.close()
    return location

#==============================================================================

