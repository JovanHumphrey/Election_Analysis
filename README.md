#**Election Results Analysis with Python**<br>

##**Overview**<br>
For this project I assisted the Colorado Board of Elections with the results of a recent congressional election. My task was to tally the total votes cast, the total votes for each candidate, the percentage of votes for each candidate, and find the winner of the election of the popular vote. In the past these calculations were determined with Excel, but the board wanted to automate the process.<br>

###**Purpose**<br>
The purpose of this project is twofold:<br>

•	Tabulate the results of the election.<br>
•	Provide a code that can be applied to future elections in the state.<br>

###**Background**<br>
After the election, votes were collected and tallied. Once counted, the board put the results in a file called election_results.csv. My job was to create a vote count report to certify the results of the election (PyPoll.py). I then had the results print to a text file to give back to the board (election_analysis.txt).
My code needed to be able to deliver the following information:<br>

•	Display the total number of votes cast.<br>
•	Display a complete list of candidates with total number of votes, and the percentage of votes for each candidate.<br>
•	Declare the winner of the election based on popular vote.<br>

##**Results**<br>

###**Explaining the Code of the Document PyPoll.py**<br>

Line 1-5: The asks.<br>
Line 7-13: Where to retrieve the CSV file and where to save the text file.<br>
Line 15-20: Initialize objects for all candidates: vote counts, list of candidates, dictionary of candidates and votes.<br>
Line 22-25: Initialize objects for the winner: candidate name, vote count, and winning percentage.<br>
Line 27-29: Open and read the CSV file.<br>
Line 31-32: Once opened, skip over the header row.<br>
Line 33-46: For loop:<br>
1.	Calculate the total votes.
2.	Find unique instances of candidates and add to Candidate List.<br>
3.	Calculate the number of votes per candidate.<br>
4.	Add that information to the dictionary.<br>

Line 48-56: Save and print election results to TXT file.<br>
Line 58-72: Save and print the vote count of each candidate to the TXT file. Calculate, save, and print the vote percentages for each candidate to the TXT file.<br>
Line 74-88: Determine the winner and print results to TXT file.<br>
<br>
**Determining the Winner**<br>

A candidate can win an election with less than half of the votes, so I couldn't simply tell the code to determine the winner by whoever got 50% or more. I needed the code to be able to figure out which candidate got the most votes, (and highest percentage).

On Lines 22-25 before the file was opened and rows looped through, it was necessary that I declare variables for the winner category. The winning candidate object would be filled with the winner's name after running the code. The winning count and percentages objects would display the winning totals after running.

On Lines 75-78 I looped through the results to determine the winner. I used an if/then statement with two values:<br>
1.	**If** the votes a candidate got were greater than (winning_count) **AND**...<br>
2.	the percentage of votes a candidate got was greater than (winning_percentage) **then** the statement was true, and thus the winner would be declared. <br>

This code would work no matter how many or how few candidates are in an election, as it compares each candidate's results against each other. See below for an explanation.<br>

Iterating through the list, the code determined that Charles Casper Stockham got more than the initial vote count and vote percentage, (both initially set at 0%). Charles Casper Stockham would be the first winner in the loop. Their vote count and percentage became the new winning totals, but the loop wasn't done. The loop then checked the next candidate Diana DeGette's results, and determined that they got more votes and a higher percentage than Charles Casper Stockham. Diana DeGette's totals replaced Charles Casper Stockham's and they became the winner. The loop continued through the final candidate: Raymon Anthony Doane. This candidate did not have more votes nor a higher percentage than the declared winner, so the winner information didn't change. In the end with 73.8% of the vote (272,892 total) Diana DeGette was declared the winner.<br>

**Challenge**<br>

My clients were happy with the results of my code. They asked me to do one more thing: add code so that county information could be tracked. Specifically, they wanted the code to track the number of votes per county, the percentage of votes per county, and declare the county with the largest voter turnout.<br>

My original code was put into a new document: PyPoll_Challenge.py and I made my additions to it. The additions were simple as the county information mirrored the candidate information. I created initialized objects for the county list (Line 15), a dictionary to hold votes per county (Line 16), and objects for the "winner" county, (aka the county with the greatest turnout: Lines 24-26). While looping through the rows to find candidate information I nested the code so that it would also look for county information. Then I created code to calculate county totals, added total votes to the dictionary, and print the results (Lines 90-102).<br>

After this was completed, I wrote an if/then statement to determine the county with the largest turnout and print the results (Lines 105-117). This worked much like the code for the election winner by looping through a list to find the county with the largest number of votes and largest percentage of votes. The "winner" was Denver with a total of 306,055 votes accounting for 82.8% of the total. Finally, these results were printed to the TXT file.

####**Summary**<br>

In summary this code was able to determine the results for this congressional election. However, it could easily be adapted to an election with more candidates and more counties without having to rewrite the code.<br>

The code works perfectly except for the printed text file. Due to my inexperience as a programmer, I was not able to solve two problems:<br>
1.	In the county votes results “Arapahoe” is listed twice.<br>
2.	There should be a line separating the county results from the election results.<br>

After assessment of this challenge, I will correct these issues and revise the README document.<br>
