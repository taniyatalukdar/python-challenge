#modules
import os
import csv
from turtle import clear

#files to read
bank_csv = os.path.join("Resources", "budget_data.csv")

#define variables
totalNumberOfMonths = 0
net_loss_profit = 0
bank_value = 0
change = 0

profits = []


with open(bank_csv) as budget_data:
    csvreader = csv.reader(budget_data)

    csv_header = next(csvreader)

     #grab first row
    first_row = next(csvreader)
    for row in csvreader:
        #total numner of months
     totalNumberOfMonths += 1
      #the net amount of profit and loss
     net_loss_profit += int(row[1])
    
     
     change = int(row[1]) - bank_value
     profits.append(change)
    


     
      

print(f"Total Months: {totalNumberOfMonths}")
print(f"Total: ${net_loss_profit}")
#print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")