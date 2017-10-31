from read_dataset import readline, split, set_input
from checkEachInputStructure import *
from write_dataset import WriteToFile, set_outputs
from donation_info import Donation
import sys


# Define Some variables
lineCounter = 1
finalResaultsForMedianValsbyzip = []
finalResaultsForMedianValsByDate = []


set_input(sys.argv[1])
set_outputs(sys.argv[2], sys.argv[3])
# Main Loop Until the Last Line
while readline(lineCounter) is not None:
    rawLine = readline(lineCounter)
    splittedRawLine = split(rawLine)
    new_donation = Donation(splittedRawLine[0], splittedRawLine[10][:5],
                            splittedRawLine[13], splittedRawLine[14], splittedRawLine[15])

    if new_donation.has_other_id() and new_donation.is_valid_to_check():
        # Considering just for medianvals_by_zip
        if new_donation.has_valid_zip():
            Donation.comparison_mode = 1 # it mean   val_by_zip
            try:
                index = finalResaultsForMedianValsbyzip[::-
                                                        1].index(new_donation)
                old_donation = finalResaultsForMedianValsbyzip[-index - 1]
                old_donation = old_donation.copy()
                old_donation.increase_number()
                old_donation.increase_amount(new_donation.transaction_amt)
                old_donation.update_median()
                finalResaultsForMedianValsbyzip.append(old_donation)
            except ValueError as err:
                finalResaultsForMedianValsbyzip.append(new_donation)

        # Considering just for medianvals_by_date
        if new_donation.has_valid_date():
            Donation.comparison_mode = 2  # it mean   val_by_date
            try:
                index = finalResaultsForMedianValsByDate.index(new_donation)
                old_donation = finalResaultsForMedianValsByDate[index]
                old_donation.increase_number()
                old_donation.increase_amount(new_donation.transaction_amt)
                old_donation.update_median()
            except ValueError as err:
                finalResaultsForMedianValsByDate.append(new_donation)

    lineCounter = lineCounter + 1

finalResaultsForMedianValsByDate.sort()
WriteToFile(finalResaultsForMedianValsbyzip, finalResaultsForMedianValsByDate)