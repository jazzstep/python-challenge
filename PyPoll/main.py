import os
import csv

pypoll = os.path.join("..", "Resources", "election_data.csv")
# Lists to store data
# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(pypoll, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    