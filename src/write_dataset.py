from donation_info import Donation

def WriteToFile(finalResaultsForMedianValsbyzip,finalResaultsForMedianValsByDate):
    file = open("../output/medianvals_by_zip.txt" , "w")
    Donation.comparison_mode = 1
    for i in range(len(finalResaultsForMedianValsbyzip)):
        file.write(str(finalResaultsForMedianValsbyzip[i]))
        file.write("\n")
    file.close()
    
    file = open("../output/medianvals_by_date.txt" , "w")
    Donation.comparison_mode = 2
    for i in range(len(finalResaultsForMedianValsByDate)):
        file.write(str(finalResaultsForMedianValsByDate[i]))
        file.write("\n")
    file.close()
    
    