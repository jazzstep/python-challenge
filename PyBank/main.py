import os
import csv
#set path to file
csvpath = os.path.join("..", "Resources", "budget_data.csv")
#set path to write output file to
output_path = os.path.join("pybanktxt.txt")
#to find number of months
count_months = []
#to save the profit/loss value of a previous year
lastyr = None
#to save the profit/loss value of a current year
currentyr =None
#save the difference between a current year and a last year
difference = None
#this will save the difference between a year and a previous year into a list
P_L = []
#to find net total
net_total = 0
#to find greatest increase in profit
great_inc = 0
# to find the month of greatest increase in profits
inc_month = None
#to find greatest decrease in profit
great_dec = 100000000
#to find month of greatest decrase in profits
dec_month = None
#to keep track of rows
counter = 1
#open up the files
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    #skip the header rows
    n= next(csvreader)
    #set up the for loop to iterate over the rows
    for row in csvreader:
        #putting what is in row[0] into the list count_months
        count_months.append(row[0])
        #net total iterating over each row to sum up the total revenue
        net_total+=int(row[1])
        #special case because the first profit/loss value doesn't have a previous value to use to find a difference with
        if counter ==1:
            #save lastyr to be the value of what is in the profit/loss column for that row
            #taking the value of what's in row[1] as an integer, because otherwise it would be a string
            lastyr = int(row[1])
        else:
            #moving onto the next row, save the value the associated profit/loss value
            currentyr = int(row[1])
            #subtract last year from current year profit/loss, and then stick that value in P_L
            #append difference in P_L, which is why currentyr-lastyr is inside the paranthesis
            difference = currentyr-lastyr
            P_L.append(difference)
            #whenever difference is greater than great_inc, save the bigger number in great_inc so you end up with the biggest
            if difference > great_inc:
                great_inc = difference
                #save the month so you can display it later
                inc_month = row[0]
            #whenever the value in "difference" is smaller than great_dec, save the smaller number so you can end up with the smallest one
            if difference < great_dec:
                great_dec = difference
                #save the month
                dec_month = row[0]
            #set last year to be current year so that we can use the value later
            lastyr = currentyr
        #move the counter forward so that we can continue iterating over the rows
        counter = counter +1
    output = (
        f"\nFinancial Analysis\n"
        f"\n------------------\n"
        f"Total Months: {len(count_months)}\n"
    #round answers to 2 decimal points using round function
        f"Average Change: {round(sum(P_L)/len(P_L),2)}\n"
        f"Total: ${net_total}\n"
        f"Greatest Increase in Revenue: {inc_month} (${great_inc})\n"
        f"Greatest Decrease in Revenue: {dec_month} (${great_dec})\n")
    print(output)
    #save to text file
    with open(output_path, mode='w',) as pybanktxt:
        pybanktxt.write(output)

