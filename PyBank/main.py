import os
import csv

# Set up variables to hold financial analysis data
total_months = 0
net_total = 0
profit_changes = []
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

# Read in the budget_data.csv file
with open("Resources/budget_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip header row
    next(csvreader)
    # Loop through each row of data
    for row in csvreader:
        # Count the total number of months
        total_months += 1
        # Add the profit/loss to the net total
        net_total += int(row[1])
        # Calculate the change in profit/loss from the previous month
        if total_months > 1:
            profit_changes.append(int(row[1]) - prev_profit)
            # Check for greatest increase/decrease in profits
            if int(row[1]) - prev_profit > greatest_increase["amount"]:
                greatest_increase["date"] = row[0]
                greatest_increase["amount"] = int(row[1]) - prev_profit
            elif int(row[1]) - prev_profit < greatest_decrease["amount"]:
                greatest_decrease["date"] = row[0]
                greatest_decrease["amount"] = int(row[1]) - prev_profit
        # Store the current month's profit/loss for use in the next iteration
        prev_profit = int(row[1])

# Calculate the average change in profit/loss
average_change = sum(profit_changes) / len(profit_changes)

# Format the results as a string
results_str = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["amount"]})
Greatest Decrease in Profits: {greatest_decrease["date"]} (${greatest_decrease["amount"]})"""

# Print the results to the terminal
print(results_str)

# Write the results to the output file
with open("analysis/financial_analysis.txt", "w", newline='') as output_file:
    output_file.write(results_str)