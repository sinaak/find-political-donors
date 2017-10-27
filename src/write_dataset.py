

def WriteToFile(finalResaultsForMedianValsbyzip,finalResaultsForMedianValsByDate):
    file = open("../output/medianvals_by_zip.txt" , "w")
    for i in range(len(finalResaultsForMedianValsbyzip)):
        file.write(finalResaultsForMedianValsbyzip[i])
        file.write("\n")
    file.close()
    
    file = open("../output/medianvals_by_date.txt" , "w")
    for i in range(len(finalResaultsForMedianValsByDate)):
        file.write(finalResaultsForMedianValsByDate[i])
        file.write("\n")
    file.close()
    
    