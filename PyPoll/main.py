# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

#Initialize variables
TotalCount = 0
KhanCount = 0
CorreyCount = 0
LiCount = 0
TooleyCount = 0
max_votecount = 0

#Function for % calculation
def percentage (part, whole):
    return 100 * float(part)/float(whole)

#Open and read CSV file
with open(csvpath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')

     for row in csvreader:
         voterid = row[0]
         country = row[1]
         candidate = row[2]
         # Find Total Vote Count
         TotalCount = TotalCount + 1

         # Find votecount by candidates
         if candidate =="Khan":
            KhanCount = KhanCount + 1
         if candidate =="Correy":
            CorreyCount = CorreyCount + 1
         if candidate =="Li":
            LiCount = LiCount + 1
         if candidate =="O'Tooley":
            TooleyCount = TooleyCount + 1
            
# Dictionary list for candidate and votes
     candidatevote = {"Khan": KhanCount,"Correy": CorreyCount,"Li" :LiCount, "O'Tooley": TooleyCount}
     # Find winner by comparing the votes they received 
     for candidate, value in candidatevote.items():
         if value > max_votecount:
            max_votecount = value
            winner = candidate
# Print results       
print(f'Election Results')
print(f'-------------------------------')
print(f'Total Votes: {TotalCount}')
print(f'-------------------------------')
print(f'Khan: {percentage(KhanCount,TotalCount):.3f}%  ({KhanCount})')
print(f'Correy: {percentage(CorreyCount,TotalCount):.3f}%  ({CorreyCount})')
print(f'Li: {percentage(LiCount,TotalCount):.3f}%  ({LiCount})')
print(f'O\'Tooley: {percentage(TooleyCount,TotalCount):.3f}%  ({TooleyCount})')
print(f'--------------------------------')
print(f'Winner: {winner} ')
print(f'--------------------------------')