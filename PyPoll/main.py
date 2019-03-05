import os
import csv
#to tally number of voters
total_voters = []
#FINAL list of candidates, with each name appearing once
candidates = []
#list of candidates, with each name appearing as many times as people voted for them
candidate_names= []
#counter to tally how many timess each person was voted for
candidate_votes = {}
#connect to file
csvpath = os.path.join("..", "Resources", "election_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header
    n = next(csvreader)
    #iterate over rows
    for row in csvreader: 
        #count number of voters by creating a list, so that we can use the len function on it later
        total_voters.append(row[0])
        #creating huge list of candidate names
        candidate_names = row[2]
        #if a name is new, ie not in the list "candidates" already, add the new name
        if candidate_names not in candidates:
            candidates.append(candidate_names)
    #count the number of votes per candidate by counting how many times their name comes up in column 3, by using a dictionary
    def CountFrequency(candidate_names):
        for candidate_votes in candidate_names:
            if(candidate_votes in candidate_names):
                candidate_names[candidate_votes]+=1
            else:
                candidate_names[candidate_votes] = 1
        for key, value in candidate_names.items():
            print("%d:%d"%(key,value))

    output = (
        f"\nElection Results\n"
        f"\n------------------\n"
        f"\nTotal votes: {len(total_voters)}\n"
        f"\n{candidates[0]}\n"
        f"\n{candidates[1]}\n"
        f"\n{candidates[2]}\n"
        f"\n{candidates[3]}\n")
    print (output)
    print("%d:%d"%(key,value))

    