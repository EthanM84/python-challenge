import os
import csv

# Set up variables to hold election analysis data
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# Read in the election_data.csv file
with open("Resources/election_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip header row
    next(csvreader)
    # Loop through each row of data
    for row in csvreader:
        # Count the total number of votes
        total_votes += 1
        # Add the candidate's vote to their total
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculate the percentage of votes each candidate won and find the winner
for candidate, votes in candidates.items():
    percentage = votes / total_votes * 100
    candidates[candidate] = {"votes": votes, "percentage": percentage}
    if votes > winner["votes"]:
        winner["name"] = candidate
        winner["votes"] = votes

# Format the results as a string
results_str = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------"""
for candidate, data in candidates.items():
    results_str += f"""\n{candidate}: {data["percentage"]:.3f}% ({data["votes"]})"""
results_str += f"""\n-------------------------
Winner: {winner["name"]}
-------------------------"""

# Print the results to the terminal
print(results_str)

# Write the results to the output file
with open("analysis/election_results.txt", "w", newline='') as output_file:
    output_file.write(results_str)
