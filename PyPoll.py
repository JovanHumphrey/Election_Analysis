# TASK 1: Calculate the total number of votes cast
# TASK 2: Print a complete list of candidates who received votes
# TASK 3: Calculate total number of votes each candidate received
# TASK 4: Calculate percentage of votes each candidate won
# TASK 5: Declare the winner of the election based on popular vote

# Add our dependencies.
import csv
import os
# Load file from path
file_to_load = os.path.join("Resources", "election_results.csv")
# Save file to path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter as 0.
total_votes = 0
# Initialze candidate list as empty.
candidate_list = []
# Initialize votes percandidate as 0.
votes_per = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_results:
    file_reader = csv.reader(election_results)

    # Skip header row in count.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # 1. Add to the total vote count.
        total_votes += 1
        # 2. Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate then...
        if candidate_name not in candidate_list:
            # ...add to Candidate List...
            candidate_list.append(candidate_name)
            # and start tracking that candidate's voter count.
            votes_per[candidate_name] = 0
        # Add a vote to that candidate's count.
        votes_per[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the election results to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in votes_per:

        # Retrieve vote count and percentage for candidate.
        votes = votes_per[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)