from read_dataset import readline,split
from checkEachInputStructure import *
from write_dataset import WriteToFile


#Define Some variables
lineCounter=1
finalResaultsForMedianValsbyzip=[]
finalResaultsForMedianValsByDate=[]
ax=0
bx=0




#Main Loop Until the Last Line
while readline(lineCounter) is not None:    
    #print(lineCounter)
    rawLine = readline(lineCounter)
    splittedRawLine = split(rawLine)
    CMTE_ID = splittedRawLine[0]
    ZIP_CODE = splittedRawLine[10][:5]
    TRANSACTION_DT = splittedRawLine[13]
    TRANSACTION_AMT = splittedRawLine[14]
    OTHER_ID = splittedRawLine[15]
  
    if checkDataLimitationForOtherID(OTHER_ID) == True and checkCMTEID_and_TransactionAmount_structure(CMTE_ID,TRANSACTION_AMT) == True:
  #Considering just for medianvals_by_zip     
        if checkZipcodeStructure(ZIP_CODE) ==True :
            
            if len(finalResaultsForMedianValsbyzip)==0: # just append the fist eligible line
                input = CMTE_ID+"|"+ZIP_CODE+"|"+TRANSACTION_AMT+"|"+"1"+"|"+TRANSACTION_AMT
                finalResaultsForMedianValsbyzip.append(input)
                
               
            else: # at least len(finalResauls)>=1
                for i in range(len(finalResaultsForMedianValsbyzip)):
                    finalResaultsForMedianValsbyzip.reverse()
                    splittedFR = finalResaultsForMedianValsbyzip[i].split("|")
                    tempCMTE_ID = splittedFR[0]
                    tempZIP_CODE = splittedFR[1]
                    Median = splittedFR[2]
                    NumberOfSimilarity = splittedFR[3]
                    TotalAmountOfDonation = splittedFR[4]
                    finalResaultsForMedianValsbyzip.reverse()
                    if tempCMTE_ID == CMTE_ID and tempZIP_CODE == ZIP_CODE:
                        #print(":D")
                        NewTRANSACTION_AMT=int(TotalAmountOfDonation)+int(TRANSACTION_AMT)
                        NewNumberOfSimilarity = int(NumberOfSimilarity)+1
                        NewMedian = DesideRounding(NewTRANSACTION_AMT/NewNumberOfSimilarity)  #problem rounding!!
                        input = CMTE_ID+"|"+ZIP_CODE+"|"+str(NewMedian)+"|"+str(NewNumberOfSimilarity)+"|"+str(NewTRANSACTION_AMT)
                        finalResaultsForMedianValsbyzip.append(input)
                        ax=1
                        #print("vaaaaaaayyyyy")
                        break
                    
                if ax==0:
                    input = CMTE_ID+"|"+ZIP_CODE+"|"+TRANSACTION_AMT+"|"+"1"+"|"+TRANSACTION_AMT
                    finalResaultsForMedianValsbyzip.append(input)
                else:
                    ax=0

    #Considering just for medianvals_by_date                  
        if checkTransactionDateStructure(TRANSACTION_DT) ==True:
            
            if len(finalResaultsForMedianValsByDate)==0: # just append the fist eligible line
                input = CMTE_ID+"|"+TRANSACTION_DT+"|"+TRANSACTION_AMT+"|"+"1"+"|"+TRANSACTION_AMT
                finalResaultsForMedianValsByDate.append(input)
                
            else:
                for i in range(len(finalResaultsForMedianValsByDate)):
                    splittedFR = finalResaultsForMedianValsByDate[i].split("|")
                    tempCMTE_ID = splittedFR[0]
                    tempTRANSACTION_DT = splittedFR[1]
                    Median = splittedFR[2]
                    NumberOfSimilarity = splittedFR[3]
                    TotalAmountOfDonation = splittedFR[4]
                    if tempCMTE_ID == CMTE_ID and tempTRANSACTION_DT == TRANSACTION_DT:
                        NewTRANSACTION_AMT = int(TotalAmountOfDonation) + int(TRANSACTION_AMT)
                        NewNumberOfSimilarity = int(NumberOfSimilarity)+1
                        NewMedian = DesideRounding(NewTRANSACTION_AMT/NewNumberOfSimilarity)
                        del finalResaultsForMedianValsByDate[i]
                        input = CMTE_ID+"|"+TRANSACTION_DT+"|"+str(NewMedian)+"|"+str(NewNumberOfSimilarity)+"|"+str(NewTRANSACTION_AMT)
                        finalResaultsForMedianValsByDate.append(input)
                        bx=1
                        break
                if bx==0:
                    input = CMTE_ID+"|"+TRANSACTION_DT+"|"+TRANSACTION_AMT+"|"+"1"+"|"+TRANSACTION_AMT
                    finalResaultsForMedianValsByDate.append(input)
                else:
                    bx=0
    
    lineCounter = lineCounter+1
    

print(finalResaultsForMedianValsbyzip[4])
print(finalResaultsForMedianValsByDate[1])
WriteToFile(finalResaultsForMedianValsbyzip,finalResaultsForMedianValsByDate)


#TEST
#print(OTHER_ID)
#print(CMTE_ID)
#print(TRANSACTION_AMT)
#print(checkDataLimitationForOtherID(OTHER_ID))
#print(checkCMTEID_and_TransactionAmount_structure(CMTE_ID,TRANSACTION_AMT))
#print(checkTransactionDateStructure(TRANSACTION_DT))
#print(checkZipcodeStructure(ZIP_CODE))
