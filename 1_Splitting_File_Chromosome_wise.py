for i in range (1, 26):
    f_m = open ("/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Genetic_Data_QC/BC_h550/Splitted_CHR/" + str(i) + ".txt", 'w', 1)
    f_m.write ("Chr" + "\t" + "ID" + "\t" + "CM" + "\t" + "Pos" + "\t" + "Alt" + "\t" + "Ref" + "\n")
    with open ("/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Genetic_Data_QC/BC_h550/BC_h550_g05_hw0001.bim", 'r') as bimfile:
        for line in bimfile:
            line_list = line.split ("\t")
            if (int (line_list [0]) == i):
                f_m.write (line)
