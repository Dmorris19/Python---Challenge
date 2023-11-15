import csv
import os

# Pull data from the CSV file
def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

# Analyze all the votes collected
def analyze_votes(data):
    # declare variables we are using
    total_votes = 0
    candidates = {}
    
    # Count votes for each candidate
    for row in data:
        total_votes += 1
        candidate = row["Candidate"]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

    # Calculate percentages of votes 
    percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

    # Calculate who is the winner
    winner = max(percentages, key=percentages.get)

    return total_votes, candidates, percentages, winner

# Print the results
def print_results(total_votes, candidates, percentages, winner):
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    
    for candidate, votes in candidates.items():
        percentage = percentages[candidate]
        print(f"{candidate}: {percentage:.3f}% ({votes})")

    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

# write the results in a text file
def save_results_to_file(total_votes, candidates, percentages, winner, output_file="election_results.txt"):
    with open(output_file, "w") as file:
        file.write("Election Results\n")
        file.write("-------------------------\n")
        file.write(f"Total Votes: {total_votes}\n")
        file.write("-------------------------\n")
        
        for candidate, votes in candidates.items():
            percentage = percentages[candidate]
            file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        file.write("-------------------------\n")
        file.write(f"Winner: {winner}\n")
        file.write("-------------------------\n")

if __name__ == "__main__":
    # locate the current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # the relative path that to follow to get to the CSV file
    relative_path = os.path.join("OfficialPyPoll", "resources", "Poll_data.csv")

    # Read and analyze the data
    data = read_csv(relative_path)
    total_votes, candidates, percentages, winner = analyze_votes(data)

    # Print and save the results
    print_results(total_votes, candidates, percentages, winner)
    save_results_to_file(total_votes, candidates, percentages, winner)


 





