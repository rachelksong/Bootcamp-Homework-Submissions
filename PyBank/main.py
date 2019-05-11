import os
import csv

#Set csv path
csvpath = os.path.join('Resources/budget_data.csv')

#Set variables
total_month = 0
total_revenue = 0
current_month_revenue = 0
last_month_revenue = 0
revenue_change = 0
revenue_changes = []
months = []

#with, open csv file
with open(csvpath, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

#total number of months / loop
    for row in csvreader:
        total_month = total_month + 1
        months.append(row[0])

#monthly changes in revenue     
        current_month_revenue = int(row[1])
        total_revenue = total_revenue + current_month_revenue
        if total_month > 1:
            revenue_change = current_month_revenue - last_month_revenue
            revenue_changes.append(revenue_change)
        last_month_revenue = current_month_revenue

#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
sum_rev_changes = sum(revenue_changes)
average_change = sum_rev_changes / (total_month - 1)
max_change = max(revenue_changes)
min_change = min(revenue_changes)
max_month_index = revenue_changes.index(max_change)
min_month_index = revenue_changes.index(min_change)
max_month = months[max_month_index]
min_month = months[min_month_index]

#print financial analysis
print(f'Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_month}')
print(f'Total: ${total_revenue}')
print(f'Average Change: ${average_change:.2f}')
print(f"Greatest Increase in Profits: {max_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_change})")