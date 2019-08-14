import os
import csv

# Path to collect data from the Resources folder
bank_csv = os.path.join('Resources', 'budget_data.csv')

# Declare variables and set starting value
total_months = 0
net_profit_loss = 0
greatest_increase = 0
greatest_decrease = 0
average_change = 0.00

# Read in the CSV file
with open(bank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    Gain_Loss = []
    Change = []

    # Loop through the data
    for row in csvreader:
        Gain_Loss.append(row[1])

        # Update greatest increase and decrease based on conditional statements
  
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
        elif int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
        
        # Add 1 month and sum profit/loss for each row
        total_months += 1
        

# Calculate average change in profit/loss
   
    for c in range(total_months-1):
        Change.append(float(Gain_Loss[c+1])-float(Gain_Loss[c]))

    average_change = sum(Change)/len(Change)
    
    
 # Print out the bank results
print(f"Financial Analysis")
print(f"-------------------------------------")
print(f"Total Months: {total_months}")
print(f"Net Profit/Loss: ${net_profit_loss}")
print(f"Average Monthly Change: ${round(average_change,2)}")
print(f"Greatest Increase in Profits: ${greatest_increase}")
print(f"Greatest Decrease in Profits: ${greatest_decrease}")

# Specify the file to write to
output_path = os.path.join("Output", "bank_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
file = open(output_path, 'w')

# Define text in each line
line1 = f"Financial Analysis" 
line2 = f"-------------------------------------"
line3 = f"Total Months: {total_months}"
line4 = f"Net Profit/Loss: ${net_profit_loss}"
line5 = f"Average Monthly Change: ${round(average_change,2)}"
line6 = f"Greatest Increase in Profits: ${greatest_increase}"
line7 = f"Greatest Decrease in Profits: ${greatest_decrease}"

# Write to the text file row by row
file.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6, line7))
file.close
