#from multiprocessing.sharedctypes import Value
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
     
     #loop through
    for row in csvreader:
     candidate = row[2]   
     
     if candidate in votesByCandidate:
       votesByCandidate.append(candidate)
       votesByCandidate[candidate] = 0
       votesByCandidate[candidate]+=1
     winner = max(votesByCandidate, key=votesByCandidate.get)
     maxVotesCount = votesByCandidate[winner]              
     rowOfVotes = sum(votesByCandidate.values())
     
     #for x in  candidate:
     #completeListCandidates.add(row[2])
 
     
    # Add to percent_votes list 
     

    for k,v in votesByCandidate.items():
      #percentageOfVotes.append((f"{v/rowOfVotes}"%))
       percentage = round((v/rowOfVotes)*100,3)
       votesByCandidate[k] = f"{percentage}%"

output_file = 'Resources/election_results.txt'
with open(output_file, "w", newline="") as datafile:    
    

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {rowOfVotes}")
    #print(f"{votesByCandidate} {percentageOfVotes:.3f}%")
    print(f"{votesByCandidate}")
    #print(f"{percentageOfVotes}")
    print("-------------------------")

    datafile.write(f"Election Results\n")
    datafile.write(f"--------------------\n")
    datafile.write(f"Total Votes: {rowOfVotes}\n")
    datafile.write(f"--------------------\n")
#for i in range(len(completeListCandidates)):
   # print(f"{completeListCandidates[i]: {str(percentageOfVotes[1])} ({str(num_votes[i])})}")
print(f"Winner: {winner}")


