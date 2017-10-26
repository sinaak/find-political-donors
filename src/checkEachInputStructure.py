

def checkDataLimitationForOtherID(Other_ID):
    if not Other_ID:
        return True # if input has no Other_ID
    else:
        return False # if input has Other_ID


def checkTransactionDateStructure(Transaction_date):

    if Transaction_date.isdigit() == False:
        return False
    elif len(Transaction_date) == 8 and int(Transaction_date[:2])<=12 and int(Transaction_date[2:4])<=31:
        return True
    else:
        return False

def checkZipcodeStructure(Zipcode):
    if len(Zipcode)>4 and len(Zipcode)<10:
        return True
    else:
        return False
    
    
def checkCMTEID_and_TransactionAmount_structure(CMTE_ID,Transaction_AMT):
    if  CMTE_ID and Transaction_AMT:
        return True
    else:
        return False
    

def DesideRounding(RawMedian):
    return int(RawMedian+0.5)