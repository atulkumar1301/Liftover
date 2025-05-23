import gzip
from multiprocessing import Pool

def chr (i):
    f_m = open ("/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Genetic_Data_QC/FinnHap550/Merged_CHR/SNP_Merged_" + str(i) + ".txt", 'w', 1)
    f_m_1 = open ("/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Genetic_Data_QC/FinnHap550/Missing_CHR/SNP_Missing_" + str(i) + ".txt", 'w', 1)
    with open ("/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Genetic_Data_QC/FinnHap550/Splitted_CHR/23.txt", 'r') as SNPfile:
        for line in SNPfile:
            c = 0
            line_list = line.split ("\t")
            with gzip.open ("/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Data/dbSNP_GB_38/All_20180418_" + str(i) + ".vcf.gz", 'rb') as dbsnp38:
                for line_db in dbsnp38:
                    line_de_db = line_db.decode ().strip()
                    line_de_db_list = line_de_db.split ("\t")
                    if "\t" not in line_de_db:
                        print ("Skipping the comment lines for chr ", i)
                    else:
                        if (line_list [1] == line_de_db_list [2]):
                            f_m.write (line.rstrip () + "\t" + line_de_db + "\n")
                            c = c + 1
                            break
        if c == 0:
            f_m_1.write (line)

if __name__ == '__main__':
    p = Pool ()
    #p.map (chr, range (1, 23))
    p.map (chr, 'X')
