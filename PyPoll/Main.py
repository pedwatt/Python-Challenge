# import needed libraries
import os
import csv
import math

# set path to source CSV
csvpath = os.path.join('Resources',  'election_data.csv')
Counter = 0
Khan_Counter = 0
Correy_Counter = 0
Li_Counter = 0
Tooley_Counter = 0
Winner = ""
#open CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header
    csv_header = next(csvreader)
    # Read each row of data after the header
    for row in csvreader:
        Counter = Counter + 1
        if row[2] == 'Khan':
            Khan_Counter = Khan_Counter +1
        elif row[2] == "Correy":
            Correy_Counter = Correy_Counter +1
        elif row[2] == "Li":
            Li_Counter = Li_Counter +1
        elif row[2] == "O'Tooley":
            Tooley_Counter = Tooley_Counter +1

print("Khan: " + str(round(Khan_Counter/Counter * 100,0)) + "% " + "(" + str(Khan_Counter) +")")
print("Li: " + str(round(Li_Counter/Counter * 100,0)) + "% " + "(" + str(Li_Counter) + ")")
print("O'Tooley: " + str(round(Tooley_Counter/Counter * 100,0)) + "% " + "(" + str(Tooley_Counter) + ")")
print("Correy: " + str(round(Correy_Counter/Counter * 100,0)) + "% " + "(" + str(Correy_Counter) + ")")

if Khan_Counter > Correy_Counter and Khan_Counter > Li_Counter and Khan_Counter > Tooley_Counter:
    Winner = "Khan"
elif Li_Counter > Correy_Counter and Li_Counter > Khan_Counter and Li_Counter > Tooley_Counter:
    Winner = "Li"
elif Correy_Counter > Li_Counter and Correy_Counter > Khan_Counter and Correy_Counter > Tooley_Counter:
    Winner = "Correy"
else:
    Winner = "O'Tooley"
print(Winner + " Wins !!!!!!!")
    # Specify the file to write to
output_path = os.path.join( "Result.csv")

# Prepare and write out file
with open(output_path, 'w', newline='') as csvOutFile:
    csvOutWriter = csv.writer(csvOutFile, delimiter=',')
    # output lines to CSV
    csvOutWriter.writerow(["Khan: " + str(round(Khan_Counter/Counter * 100,0)) + "% " + "(" + str(Khan_Counter) +")"])
    csvOutWriter.writerow(["Li: " + str(round(Li_Counter/Counter * 100,0)) + "% " + "(" + str(Li_Counter) + ")"])
    csvOutWriter.writerow(["O'Tooley: " + str(round(Tooley_Counter/Counter * 100,0)) + "% " + "(" + str(Tooley_Counter) + ")"])
    csvOutWriter.writerow(["Correy: " + str(round(Correy_Counter/Counter * 100,0)) + "% " + "(" + str(Correy_Counter) + ")"])
    csvOutWriter.writerow([Winner + " Wins !!!!!!!"])   
