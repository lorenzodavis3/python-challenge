import os
import csv

print("Current working directory;", os.getcwd())

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# Initialize variables:
# total_months to count the number of months in the dataset.
# total_profit_losses to accumulate the total profit/losses over all months.
# previous_month_profit_losses to store the profit/losses value of the previous row/month for change calculation.
# changes to list all month-to-month changes in profit/losses.
# greatest_increase to track the date and amount of the greatest increase in profits.
# greatest_decrease to track the date and amount of the greatest decrease in profits.
total_months = 0
total_profit_losses = 0
previous_month_profit_losses = None
changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Open the CSV file
with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    # Process each row
    for row in csvreader:
        # Increment the total_months counter for each row processed.
        total_months += 1
        # Convert the second column (index 1) to an integer for profit/losses and add it to total_profit_losses.
        current_month_profit_losses = int(row[1])
        total_profit_losses += current_month_profit_losses
        
         # Calculate the change from the previous month if it's not the first month.
        if previous_month_profit_losses is not None:
            change = current_month_profit_losses - previous_month_profit_losses
            changes.append(change)
            # Check and update the greatest increase in profits if the current change is greater than the current recorded.
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
            # Check and update the greatest decrease in profits if the current change is less than the current recorded.
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]
        # Update previous_month_profit_losses to the current month's value for the next iteration.
        previous_month_profit_losses = current_month_profit_losses

# Calculate the average change in profit/losses. Check if the list is not empty to avoid division by zero.
average_change = sum(changes) / len(changes) if changes else 0

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Specify the output path for writing the results to a text file within the 'analysis' directory.
output_path = 'analysis/financial_analysis_output.txt'
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")