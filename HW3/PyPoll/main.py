
import os
import csv

#Set csv path
csvpath = os.path.join('Resources/election_data.csv')

#Set variables
total_votes = 0
candidate = ""
candidate_votes = {}
candidate_percentages ={}
winner_votes = 0
winner = ""

#with, open csv file
with open(csvpath,'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    #Count total number of votes
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1

#Vote percentage and winner
for person, vote_count in candidate_votes.items():
    candidate_percentages[person] = '{0:.0%}'.format(vote_count / total_votes)
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = person


# variable for output file
output_file = os.path.join("PyPoll_Election_Data.txt")

#Open the output file
dashbreak = "-------------------------"

with open(output_file, "w", newline="") as text_file:
   print("Election Results", file=text_file)
   print(dashbreak, file=text_file)
   print(f"Total Votes: {total_votes}", file=text_file)
   print(dashbreak, file=text_file)
   for person, vote_count in candidate_votes.items():
        print(f"{person}: {candidate_percentages[person]} ({vote_count})", file=text_file)
        print(f"Winner: {winner}", file=text_file)