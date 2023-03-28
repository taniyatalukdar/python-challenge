#modules
from code import interact
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
previousRowValue = 0

#Declaring lists
profits = []
changeInProfitLoss = []
months = []

#reading the csv file
with open(bank_csv) as budget_data:
    csvreader = csv.reader(budget_data)
    #skipping the header/ first row
    csv_header = next(csvreader)
     #skipS first row the second time
    first_row = next(csvreader)
    #calculating the value of the previous row
    previousRowValue = int(first_row[1])
    #calculating the total number of months in the csv
    totalNumberOfMonths += 1
    #calculating the total loss or profit by adding the value of each row
    net_loss_profit += previousRowValue
    
    #looping through the csv
    for row in csvreader:
        #total numner of months
     totalNumberOfMonths += 1
      #the net amount of profit and loss
     net_loss_profit += int(row[1])
     #adding the value of the rows in the list of changeInProfitLoss
     changeInProfitLoss.append(int(row[1]) - previousRowValue) 
     previousRowValue = int(row[1])
     #appending the value of months in the months list
     months.append(row[0])

#outisde the for loop, calculating the average change
averageChange = round(sum(changeInProfitLoss)/ len(changeInProfitLoss), 2)
#using the max funtion in averageChange to determine the greatest increase
greatestIncrease = max(changeInProfitLoss)
#determining the index of the greatest increase to get to the month/date
greatestIncreaseIndex = changeInProfitLoss.index(greatestIncrease)
greatestIncreaseDate = months[greatestIncreaseIndex]

#using the min funtion in averageChange to determine the greatest decrease
greatestDecrease = min(changeInProfitLoss)
greatestDecreaseIndex = changeInProfitLoss.index(greatestDecrease)
greatestDecreaseDate = months[greatestDecreaseIndex]
     
     
 #Exporting to .txt file
output_file = 'Resources/election_results.txt'
with open(output_file, "w", newline="") as datafile:    
     
         
 #printing out the results    
 print("Financial Analysis")
 print("----------------------------")
 print(f"Total Months: {totalNumberOfMonths}")
 print(f"Total: ${net_loss_profit}")
 print(f"Average Change: ${averageChange}")
 print(f"Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease})")
 print(f"Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease})")


 #writing to the .txt file
 datafile.write(f"Financial Analysis\n")
 datafile.write(f"--------------------\n")
 datafile.write(f"Total Months: {totalNumberOfMonths}\n")
 datafile.write(f"Total: ${net_loss_profit}\n")
 datafile.write("Average Change: ${averageChange}\n")
 datafile.write(f"Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease})\n")
 datafile.write(f"Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease})\n")