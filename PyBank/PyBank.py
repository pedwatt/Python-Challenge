# import needed libraries
import os
import csv

# set path to source CSV
csvpath = os.path.join('Resources',  'budget_data.csv')
Counter = 0
runningTotal = 0
currValue = 0
PreValue = 0 
diff = []
diffTotal = 0
greatest_Pos_Change_Date = "hi"
greatest_Pos_Change_Val = 0
greatest_Neg_Change_Date = "by"
greatest_Neg_Change_Val = 0
#open CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        Counter = Counter + 1
        runningTotal = runningTotal + int(row[1])
        PreValue = currValue
        currValue = int(row[1])
        # skip the first value when calculating the difference table
        if PreValue != 0: 
            diff.append(currValue-PreValue)
        # find the biggest positive change
        if int(row[1]) > int(greatest_Pos_Change_Val):
            greatest_Pos_Change_Val = currValue -PreValue
            greatest_Pos_Change_Date = row[0] 
        # find the biggest negative change    
        if int(row[1]) < int(greatest_Neg_Change_Val):
            greatest_Neg_Change_Val = currValue - PreValue
            greatest_Neg_Change_Date = row[0]     
    # sum the difference set to allow the average to be found
    for x in diff:
        diffTotal =  diffTotal + x
    print("Total Months: " + str(Counter))
    print("Total: " + str(runningTotal))
    print("Average Change: " + str(diffTotal/(Counter-1)))
    print("Greatest Increase in Profits: " + greatest_Pos_Change_Date + " " + "(" + str(greatest_Pos_Change_Val) + ")" )
    print("Greatest Decrease in Profits: " + greatest_Neg_Change_Date + " " + "(" + str(greatest_Neg_Change_Val) + ")" )
    
    # Specify the file to write to
output_path = os.path.join( "report.csv")

# Prepare and write out file
with open(output_path, 'w', newline='') as csvOutFile:
    csvOutWriter = csv.writer(csvOutFile, delimiter=',')
    # output lines to CSV
    csvOutWriter.writerow(["Total Months: " + str(Counter)])
    csvOutWriter.writerow(["Total: " + str(runningTotal)])
    csvOutWriter.writerow(["Average Change: " + str(diffTotal/(Counter-1))])
    csvOutWriter.writerow(["Greatest Increase in Profits: " + greatest_Pos_Change_Date + " " + "(" + str(greatest_Pos_Change_Val) + ")"])
    csvOutWriter.writerow(["Greatest Decrease in Profits: " + greatest_Neg_Change_Date + " " + "(" + str(greatest_Neg_Change_Val) + ")"])   