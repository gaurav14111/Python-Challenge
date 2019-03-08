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

#Finding the index value of max of iprofit_loss list to find the index and find date
max_value = max(iprofit_loss)
max_index = iprofit_loss.index(max_value)
max_date = date[max_index]


#Finding the index value of min of iprofit_loss list to find the index and find date
min_value = min(iprofit_loss)
min_index = iprofit_loss.index(min_value)
min_date = date[min_index]



print("Financial Analysis")
print("--------------------------------")
print (f"Total Months: {len(date)}")
print (f"Total: ${sum(iprofit_loss)}")
print(f"Average Change: ${Average_Change}")
print(f"Greatest Increase in Profits: {max_date} (${max_value})")
print(f"Greatest Decrease in Profits: {min_date} (${min_value})")
            