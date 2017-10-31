from donation_info import Donation

output_zip = None
output_date = None

def set_outputs(output1, output2):
    global output_zip, output_date
    output_zip = output1
    output_date = output2
    return

def WriteToFile(finalResaultsForMedianValsbyzip,finalResaultsForMedianValsByDate):
    file = open(output_zip , "w")
    Donation.comparison_mode = 1
    for i in range(len(finalResaultsForMedianValsbyzip)):
        file.write(str(finalResaultsForMedianValsbyzip[i]))
        file.write("\n")
    file.close()
    
    file = open(output_date , "w")
    Donation.comparison_mode = 2
    for i in range(len(finalResaultsForMedianValsByDate)):
        file.write(str(finalResaultsForMedianValsByDate[i]))
        file.write("\n")
    file.close()
    
    