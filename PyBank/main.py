import os
import csv
#get path
budget_data = os.path.join("..", "Resources", "budget_data.csv")
#setting variables to work with
total_months = 0
total_rev = 0
aver_change=[]
#opening the csv file
with open(budget_data, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    #get rows (minus header) because there's a month per row
    for row in csvreader:
        total_months +=1    
        total_rev +=int(row["Profit/Losses"])
    total_rev = "{:,}".format(total_rev)
    print(f"Total Months: {total_months}")
    print(f"Total Revenue: {total_rev}")

    