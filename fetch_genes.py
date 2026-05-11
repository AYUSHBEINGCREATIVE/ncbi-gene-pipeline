import csv
from Bio import Entrez

Entrez.email = "ayush.dhote.mitbio@gmail.com"
handle = Entrez.esearch(db="gene", term="Alzheimers disease", retmax=10)
record = Entrez.read(handle)
handle.close()
print(record['IdList'])
ids = record['IdList']
handle = Entrez.efetch(db="gene", id=",".join(ids), rettype="docsum", retmode="xml")
records = Entrez.read(handle)
handle.close()
print(records['DocumentSummarySet']['DocumentSummary'][0])
gene = records['DocumentSummarySet']['DocumentSummary'][0]
print(gene['Name'])
print(gene['Description'])
print(gene['Chromosome'])


with open("alzheimers_genes.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Gene ID", "Name", "Description", "Chromosome", "Organism"])
    
    for gene in records['DocumentSummarySet']['DocumentSummary']:
        writer.writerow([
            gene.attributes['uid'],
            gene['Name'],
            gene['Description'],
            gene['Chromosome'],
            gene['Organism']['ScientificName']
        ])
