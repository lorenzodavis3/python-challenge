import os
import csv

print("Current working directory;", os.getcwd())

# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources', 'election_data.csv')

# Initialize a dictionary to count votes for each candidate
vote_counts = {}

# Step 1: Read the CSV file
with open(election_data_csv, 'r') as csvfile:
    # Use DictReader for easier access to columns by header names.
    reader = csv.DictReader(csvfile, delimiter=',')
    total_votes = 0
    # Iterate over each row in the CSV file.
    for row in reader:
        # Increment the total votes counter for each row
        total_votes += 1
        # Extract the candidate name from the 'Candidate' column
        candidate = row['Candidate']
        # Check if the candidate is already in the vote_counts dictionary.
        if candidate in vote_counts:
            # Increment the candidate's count
            vote_counts[candidate] += 1
        else:
            # Initialize the count for new candidates
            vote_counts[candidate] = 1

# Initialize dictionaries and variables to store percentage votes and track the winner.
percent_votes = {}
winner = None
max_votes = 0

# Calculate the percentage of votes each candidate received and determine the winner.
for candidate, votes in vote_counts.items():
    percent_votes[candidate] = (votes / total_votes) * 100
     # Check if the current candidate has more votes than the current max_votes.
    if votes > max_votes:
        # Update max_votes with the higher vote count
        max_votes = votes
        # Update winner to the current candidate
        winner = candidate

# Print the analysis
print('Election Results')
print('----------------------------')
print(f'Total Votes: {total_votes}')
print ('----------------------------')
# Loop through each candidate to print their vote count and percentage.
for candidate, votes in vote_counts.items():
    print(f'{candidate}: {percent_votes[candidate]:3f}% ({votes})')
print('----------------------------')
print(f'Winner: {winner}')
print('----------------------------')
    
# Define the path for the output file within the 'analysis' directory.
output_path = 'analysis/election_results.txt'
with open(output_path, 'w') as file:
    file.write('Election Results\n')
    file.write('-------------------------\n')
    file.write(f'Total Votes: {total_votes}\n')
    file.write('-------------------------\n')
    for candidate, votes in vote_counts.items():
        file.write(f'{candidate}: {percent_votes[candidate]:.3f}% ({votes})\n')
    file.write('-------------------------\n')
    file.write(f'Winner: {winner}\n')
    file.write('-------------------------\n')
# Notify the results were saved.
print(f'Results saved to {output_path}')

