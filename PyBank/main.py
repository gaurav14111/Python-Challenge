# Modules
import os
import csv


# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

#Create list for each columns
date = []
profit_loss = []
Total = 0.0
Average_Change = 0.0
# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#Read the header row first
    csv_header = next(csvfile)

    # Loop through to read the number of rows
    for row in (csvreader):
        #Total = float(row[1]) + Total
        date.append(row[0])
        profit_loss.append(row[1])
        iprofit_loss = [int(i) for i in profit_loss]
        
Average_Change = sum(iprofit_loss) / len(iprofit_loss)
print("Financial Analysis")
print("--------------------------------")
print (f"Total Months: {len(date)}")
print (f"Total: ${sum(iprofit_loss)}")
print(f"Average Change: ${Average_Change}")
print(f"Greatest Increase in Profits: (${max(iprofit_loss)})")
print(f"Greatest Decrease in Profits: (${min(iprofit_loss)})")
            