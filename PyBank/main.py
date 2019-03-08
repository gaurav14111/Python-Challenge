# Import modules required for accessing CSV file
import os
import csv


# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Declare the variables

Total_Months = 0
Total = 0.00
Average = 0.00
# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    # Loop through looking for the video
    for row in csvreader:
        Total_Months = Total_Months + 1
        Total = float(row[1]) + Total
        Average = Total/Total_Months
        
      
# Print the values
print(f'Total Months:  + Total_Months)
print(f'"Total: "+ Total)