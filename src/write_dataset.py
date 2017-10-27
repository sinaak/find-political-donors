

def WriteToFile(finalResaultsForMedianValsbyzip):
    file = open("../output/medianvals_by_zip.txt" , "w")
    for i in range(len(finalResaultsForMedianValsbyzip)):
        file.write(finalResaultsForMedianValsbyzip[i])
        file.write("\n")
    file.close()