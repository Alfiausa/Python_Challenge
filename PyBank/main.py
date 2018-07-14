# Bringing in Dependencies
import csv
import os

#Define variables to load raw data for budget
file_to_load = os.path.join('raw_data', 'budget_data_1.csv')

#Define variables to track change in revenue
total_months = 0
total_amount_of_revenue = 0
net_change_list = []
greatest_increase = ['',0]
greatest_decrease = ['', 9999999999999999999]
month_of_change = []

#Read CSV and conver to list of dictionaries
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    #Read the header row
    header = next(reader)

    #Extract first row
    first_row = next(reader)
    total_months = total_months + 1

    print(first_row)

    total_amount_of_revenue = total_amount_of_revenue + int(first_row[1])

    prev_net = int(first_row[1])

    #Iterate through every row
    for row in reader:
        #Track total number of months
        total_months = total_months + 1
        #Track total number of revenue
        total_amount_of_revenue = total_amount_of_revenue + int(row[1])
        
        #Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        #Calc the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        #Calc the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

#Calc the average net change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

#Generate=define the output Summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# output = ("hello\n")    
print(output)
