import os
import csv

# Path to collect data from the Resources folder
poll_csv = os.path.join('Resources', 'election_data.csv')

# Declare Candidate List & Votes List
candidates_list = []
all_votes_list = []

# Declare variables and set starting value
total_votes = 0
most_votes = 0
winner = ""

# Read in the CSV file
with open(poll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

        # Populate the list of candidates and all votes
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
            all_votes_list.append(row[2])
        else:
            all_votes_list.append(row[2])
             
    # Calculate the total number of votes and winner
    for i in candidates_list:
        total_votes = total_votes + all_votes_list.count(i)

        if all_votes_list.count(i) > most_votes:
            most_votes = all_votes_list.count(i)
            winner = i

### --------------------- PRINT RESULTS ----------------------------------
 # Print out the election results
print(f"Election Results")
print(f"-------------------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------------------")

# Calculate & Print the Number of Votes for Each Candidate and store in List
for j in candidates_list:
    print(f"{j}: {round(100*(all_votes_list.count(j)/total_votes),3)}00% ({all_votes_list.count(j)})")

print(f"-------------------------------------")
print(f"Winner: {winner}")
print(f"-------------------------------------")

### --------------------- WRITE TO TXT FILE ----------------------------------
# Specify the file to write to
output_path = os.path.join("Output", "poll_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
file = open(output_path, 'w')

# Write to the text file row by row
file.writelines([
    f"Election Results \n", 
    "------------------------------------- \n",
    f"Total Votes: {total_votes} \n",
    "------------------------------------- \n"])
for line in candidates_list:
    file.write(f"{line}: {round(100*(all_votes_list.count(line)/total_votes),3)}00% ({all_votes_list.count(line)})\n")
file.writelines([
    f"------------------------------------- \n",
    f"Winner: {winner} \n",
    f"------------------------------------- \n"])    

file.close

