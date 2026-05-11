## Motivation
Alzheimer's disease affects over 55 million people worldwide. 
Identifying key genes associated with the disease is a critical 
first step in computational drug discovery pipelines. This project 
automates the gene retrieval step using NCBI's Entrez API.

# NCBI Alzheimer's Gene Retrieval Pipeline 🧬

Automated pipeline to fetch gene records associated with Alzheimer's disease 
from NCBI using the Entrez API.

## What it does
- Searches NCBI Gene database for Alzheimer's disease related genes
- Fetches gene details including name, description, chromosome, and organism
- Exports results to a structured CSV file

## Tools Used
- Python
- Biopython
- NCBI Entrez API

## Output
A CSV file containing: Gene ID, Name, Description, Chromosome, Organism

## How to run
```bash
pip install biopython
python fetch_genes.py
```

