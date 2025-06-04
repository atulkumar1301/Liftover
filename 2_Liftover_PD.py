#merge two files by specific column
import zipfile
import pandas as pd
# reading csv files
for i in range (1, 23):
	data1 = pd.read_csv("/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Genetic_Data_QC/FinnHap550/Splitted_CHR/" + str(i) + ".txt", delimiter="\t")
	data2 = pd.read_csv("/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Data/dbSNP_GB_38/All_20180418_" + str(i) + ".vcf.gz", delimiter="\t", compression='gzip', on_bad_lines='skip', comment='#',
	names=["CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO"])
	df = pd.merge(data1, data2, how='left', on='ID')
	df.to_csv ("/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Genetic_Data_QC/FinnHap550/Merged_CHR/SNP_Merged_" + str(i) + ".txt", sep="\t", index=False)
