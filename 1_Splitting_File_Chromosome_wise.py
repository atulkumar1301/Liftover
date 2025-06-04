for i in range (1, 26):
    f_m = open ("/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Genetic_Data_QC/FinnHap550/Splitted_CHR/" + str(i) + ".txt", 'w', 1)
    with open ("/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Genetic_Data_QC/FinnHap550/FinnHap550_postQC-9Sept09.bim", 'r') as bimfile:
        for line in bimfile:
            line_list = line.split ("\t")
            if (int (line_list [0]) == i):
                f_m.write (line)
