from pathlib import Path
from pathlib import PurePath
import sys
import os
import subprocess
# Loading the PLINK Module
plink2 = "/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Tools/plink2_mac_arm64_20250420/./plink2" #Change the directory accordingly

filename = "/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Genetic_Data_QC/BC_h550/BC_h550_g05_hw0001"

out_file = "/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Genetic_Data_QC/BC_h550/1_BC_h550_g05_hw0001"

pwd = "/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Genetic_Data_QC/BC_h550/"

source_dir = Path('/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Genetic_Data_QC/BC_h550/Merged_CHR/')
#files = source_dir.iterdir()
files = sorted (source_dir.glob('*.txt'))
#f_m = open ("/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Genetic_Data_QC/BC_h550/Update_variant_information/Full_Merged_File.txt", 'w', 1)
f_m_1 = open ("/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Genetic_Data_QC/BC_h550/Update_variant_information/Update_Alleles.txt", 'w', 1)
f_m_2 = open ("/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Genetic_Data_QC/BC_h550/Update_variant_information/Update_Chromosome.txt", 'w', 1)
f_m_3 = open ("/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Genetic_Data_QC/BC_h550/Update_variant_information/Update_map.txt", 'w', 1)
for file_names in files:
    with open (file_names, 'r') as myFile:
        line = myFile.readline ()
        for line in myFile:
            line_list = line.split ("\t")
            if len (line_list [9]) > 1:
                All_allele = line_list [9].split (",")
                f_m_1.write (str(line_list [1]) + "\t" + str(line_list[4]) + "," + str(line_list[5]) + "\t" + str(All_allele[0]) + "," + str(line_list[8]) + "\n")
            else:
                f_m_1.write (str(line_list [1]) + "\t" + str(line_list[4]) + "," + str(line_list[5]) + "\t" + str(line_list[9]) + "," + str(line_list[8]) + "\n")
            #CHR = line_list[6].split (".")
            f_m_2.write (str(line_list [1]) + "\t" + str(line_list[6]) + "\n")
            #POS = line_list[7].split (".")
            f_m_3.write (str(line_list [1]) + "\t" + str(line_list[7]) + "\n")

try:
   subprocess.run([plink2, "--bfile", filename, "--update-chr", "Update_variant_information/Update_Chromosome.txt", "--update-map", "Update_variant_information/Update_map.txt", "--sort-vars", "--make-pgen", "--out", out_file], check = True, capture_output=True, cwd = pwd)
except subprocess.CalledProcessError as e1:
        print ("The following error is encountered ", e1 , "\n", "Check the log file for detailed error", "\n")

out_file_1 = "/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Genetic_Data_QC/BC_h550/2_BC_h550_g05_hw0001"
try:
    subprocess.run([plink2, "--pfile", out_file, "--update-alleles", "Update_variant_information/Update_Alleles.txt", "--make-pgen", "--out", out_file_1], check = True, capture_output=True, cwd = pwd)
except subprocess.CalledProcessError as e2:
        print ("The following error is encountered ", e2, "\n", "Check the log file for detailed error", "\n")
