import os
import csv
from collections import Counter
#to tally number of voters
total_voters = []
total_votes = None
#FINAL list of candidates, with each name appearing once
candidates = {}
#list of candidates, with each name appearing as many times as people voted for them
candidate_names= []
#counter to tally how many timess each person was voted for
candidate_votes = []
ticker = 0
winner = ''
percent_list = {}
#connect to file
output_path = os.path.join("pypolltxt.txt")
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
        total_votes = len(total_voters)
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
        #if a name is new, ie not in the list "candidates" already, add the new name
        for key, value in candidates.items():
            percent_list[key] = round((value/total_votes) * 100, 1)
        for key in candidates.keys():
            if candidates[key] > ticker:
                winner = key
                ticker = candidates[key]

        #count the number of votes per candidate by counting how many times their name comes up in column 3
print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------------------")
for key, value in candidates.items():
    print(key + ": " + str(percent_list[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")

with open(output_path, mode='w',) as file:
    file.write("Election Results \n")
    file.write("------------------------------------- \n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("------------------------------------- \n")
    for key, value in candidates.items():
        file.write(key + ": " + str(percent_list[key]) + "% (" + str(value) + ") \n")
    file.write("------------------------------------- \n")
    file.write("Winner: " + winner + "\n")
    file.write("------------------------------------- \n")