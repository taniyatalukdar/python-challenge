import os
import csv
#from collections import defaultdict

#files to read
poll_csv = os.path.join("Resources", "election_data.csv")

#declaring variables
rowOfVotes = 0
percentageOfVotes = []
votesByCandidate = {}
votesToWin = 0

# open and read csv file
with open(poll_csv) as election_data:
    csvreader = csv.reader(election_data)
    
    #skip first row
    csv_header = next(csvreader)
     
     #loop through the file
    for row in csvreader:
     candidate = row[2]   
     #If candidtae is already on our list, we will simply add a vote in his/her name 
     if candidate in votesByCandidate:
       votesByCandidate[candidate]+=1
     else:  
       votesByCandidate[candidate] = 1
       
       #determine the winner by using max function to the dictionary
     winner = max(votesByCandidate, key=votesByCandidate.get)
     maxVotesCount = votesByCandidate[winner]   
     #get total number of votes by using the sum function        
     rowOfVotes = sum(votesByCandidate.values())
     
#Exporting to .txt file
output_file = 'Resources/election_results.txt'
with open(output_file, "w", newline="") as datafile:    
    
  # Displaying results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {rowOfVotes}")
    print("-------------------------")
    #looping through the votes to get the number of votes attributing to each candidate and converting to percentage
    for k,v in votesByCandidate.items():
        percentage = round((v/rowOfVotes)*100,3)
        print(f"{k}: {percentage} % ({v})\n")
    print("-------------------------")
    print(f"Winner: {winner}")
  #writing to the .txt file
    datafile.write(f"Election Results\n")
    datafile.write(f"--------------------\n")
    datafile.write(f"Total Votes: {rowOfVotes}\n")
    datafile.write(f"--------------------\n")
    for k,v in votesByCandidate.items():
        percentage = round((v/rowOfVotes)*100,3)
        datafile.write(f"{k}: {percentage} % ({v})\n")
    datafile.write("-------------------------\n")
    datafile.write(f"Winner: {winner}")

