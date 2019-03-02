#this file is too try out code ideas to address bugs I found using online ideas
import os
import csv
#get path
budget_data = os.path.join("..", "Resources", "budget_data.csv")
#setting variables to work with
total_months = 0
#opening the csv file
with open(budget_data, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    for row in csvreader:
        total_months +=1
print("Total Months: "+str(total_months))