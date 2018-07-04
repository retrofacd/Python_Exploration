import os
import csv

file_to_load = "/Users/carolineteti/Desktop/python-challenge/PyBank/raw_data/budget_data_2.csv"
file_to_output = "/Users/carolineteti/Desktop/python-challenge/PyBank/budget_analysis2.txt"

total_months = 0
total_revenue = 0

previous_revenue = 0
revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

revenue_changes = []

with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)
    for row in reader:
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Revenue"])
        print(row)
        
        revenue_change = int(row["Revenue"]) - previous_revenue
        print(revenue_change)
        
        previous_revenue = int(row["Revenue"])
        print(previous_revenue)
        
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row["Date"]
            
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row["Date"]
        
        revenue_changes.append(int(row["Revenue"]))

revenue_avg = sum(revenue_changes) / len(revenue_changes)

print()
print()
print()
print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: " + "$" + str(total_revenue))
print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")

with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")

