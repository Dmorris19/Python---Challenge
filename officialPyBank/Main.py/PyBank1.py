import csv
import os

# create the path you want to follow  
csvpath = os.path.join("OfficialPyBank", "resources", "budget_data.csv")


# declaring the variable used to keep our data
total_months = 0
total_profit_losses = 0
prev_profit_loss = 0
monthly_changes = []
dates = []


# Pull Data from the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Go over the first row which is for headers 
    header = next(csvreader)

    # using for loops we will go through every row in the csv
    for row in csvreader:
        
        
        # Pull the date and profit/loss values
        date = row[0]
        profit_loss = int(row[1])

        # Calculate the time and revenue by total months and total profit/loss
        total_months += 1
        total_profit_losses += profit_loss

        # Calculate change in profit/loss and store it along with the date
        if total_months > 1:
            change = profit_loss - prev_profit_loss
            monthly_changes.append(change)
            dates.append(date)

        # Update previous profit/loss for each loop
        prev_profit_loss = profit_loss

# Calculate average change, greatest increase, and greatest decrease
average_change = sum(monthly_changes) / (total_months - 1)
greatest_increase = max(monthly_changes)
greatest_increase_date = dates[monthly_changes.index(greatest_increase)]
greatest_decrease = min(monthly_changes)
greatest_decrease_date = dates[monthly_changes.index(greatest_decrease)]

# Print the financial analysis results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export the results to a text file
output_path = os.path.join("OfficialPyBank", "resources", "financial_analysis_results.txt")
with open(output_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit_losses}\n")
    output_file.write(f"Average Change: ${round(average_change, 2)}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

print(f"Financial analysis results exported to {output_path}")
